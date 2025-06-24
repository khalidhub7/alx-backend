import redis from 'redis';
import express from 'express';
import { promisify } from 'util';

const app = express();
const client = redis.createClient();

client
  .on('connect', () => {
    console.log(
      'Redis client connected to the server',
    );
    // clear item keys
    client.flushall(() => {});
  })
  .on('error', (err) => {
    console.log(
      `Redis client not connected to the server: ${err}`,
    );
  });

// list of products
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

// make client.get return a promise
const getAsync = promisify(client.get).bind(client);

// get product by id
const getItemById = (id) => (
  listProducts.find((obj) => obj.itemId === id)
);

// get reserved stock
const getCurrentReservedStockById = async (
  itemId) => (Number(await getAsync(`item.${itemId}`)));

// reserve item stock safely
const reserveStockById = async (itemId, stock) => {
  const value = await getAsync(`item.${itemId}`);
  const reserved = Number(value) || 0;
  const product = getItemById(itemId);

  if (!product) { throw new Error('Product not found'); }
  if (reserved + stock <= product.initialAvailableQuantity) {
    client.set(`item.${itemId}`, reserved + stock);
  } else { throw new Error('Not enough stock available'); }
};

app.get('/list_products', (_, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const id = Number(req.params.itemId);
  const product = getItemById(id);

  if (product) {
    const reservedStock = await getCurrentReservedStockById(id);
    const freeStock = product.initialAvailableQuantity - reservedStock;
    res.json({ ...product, currentQuantity: freeStock });
  } else {
    res.status(404).json({ status: 'Product not found' });
  }
});

app.get('/reserve_product/:itemId', (req, res) => {
  const id = Number(req.params.itemId);

  reserveStockById(id, 1)
    .then(() => {
      res.json({ status: 'Reservation confirmed', itemId: id });
    })
    .catch((err) => {
      if (err.message === 'Product not found') {
        res.status(404).json({ status: err.message });
      } else {
        res.status(400).json({ status: err.message, itemId: id });
      }
    });
});

app.listen(1245, 'localhost', () => {
  console.log('server running on http://localhost:1245');
});

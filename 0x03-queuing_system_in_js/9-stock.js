import Redis from 'ioredis';
import express from 'express';

const app = express();
const redis = new Redis();

(async () => {
  await redis.flushall();
})();

// data
const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5
  }
];

// find product by its ID
function getItemById (itemId) {
  for (const product of listProducts) {
    if (product.itemId === itemId) {
      return product;
    }
  }
}

// reserve stock for a product
async function reserveStockById (itemId, stock) {
  const key = `item.${itemId}`;
  try {
    await redis.set(key, stock);
  } catch (err) {
    throw new Error(
        `Error reserving stock: ${err}`);
  }
}

// check the reserved stock for a product
async function getCurrentReservedStockById (itemId) {
  const stock = await redis.get(`item.${itemId}`);
  return stock ? Number(stock) : null;
}

app.get('/list_products', (request, response) => {
  response.statusCode = 200;
  response.setHeader(
    'Content-Type', 'application/json');
  response.json(listProducts);
});

app.get('/list_products/:itemId', async (request, response) => {
  const itemId = request.params.itemId;
  const product = getItemById(Number(itemId));

  // product not found
  if (!product) {
    return response.status(404).json(
      { status: 'Product not found' });
  }

  // the available stock quantity
  let currentQuantity = await getCurrentReservedStockById(itemId);
  if (currentQuantity !== null) {
    currentQuantity = Number(currentQuantity);
  }
  if (currentQuantity === null) {
    currentQuantity = product.initialAvailableQuantity;
  }

  // give info about currentQuantity
  response.status(200).json({
    ...product,
    currentQuantity
  });
});

app.get('/reserve_product/:itemId', async (request, response) => {
  const itemId = request.params.itemId;
  const product = getItemById(Number(itemId));

  // product not found
  if (!product) {
    return response.status(404).json(
      { status: 'Product not found' });
  }

  // handle available quantity
  let currentQuantity = await getCurrentReservedStockById(itemId);
  if (currentQuantity !== null) {
    currentQuantity = Number(currentQuantity);
  }
  if (currentQuantity === null) {
    currentQuantity = product.initialAvailableQuantity;
  }

  // handle Reservation
  if (currentQuantity <= 0) {
    return response.status(400).json(
      { status: 'Not enough stock available', itemId });
  }
  if (currentQuantity > 0) {
    await reserveStockById(itemId, currentQuantity - 1);
    return response.status(200).json(
      { status: 'Reservation confirmed', itemId });
  }
});

app.listen(1245, 'localhost', () => {
  console.log('Server is running on http://localhost:1245');
});

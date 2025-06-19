import redis from 'redis';

const client = redis.createClient();

const key = 'ALX';

const obj = {
  Portland: 50, Seattle: 80, 'New York': 20,
  Bogota: 20, Cali: 40, Paris: 2,
};

const args = Object.entries(obj);

client.del(key, () => {
  args.forEach(([k, v], i) => {
    client.hset(key, k, v, (err, res) => {
      redis.print(err, res);

      if (i === args.length - 1) {
        client.hgetall(key, (_, resp) => {
          console.log(resp);
        });
      }
    });
  });
});

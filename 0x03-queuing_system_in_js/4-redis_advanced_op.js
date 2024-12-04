import { createClient, print } from 'redis';

const conn = createClient();

conn.on('error', (err) => {
  console.log(err.message);
});

conn.on('connect', () => {
  conn.hset('HolbertonSchools', 'Portland', '50', print);
  conn.hset('HolbertonSchools', 'Seattle', '80', print);
  conn.hset('HolbertonSchools', 'New York', '20', print);
  conn.hset('HolbertonSchools', 'Bogota', '20', print);
  conn.hset('HolbertonSchools', 'Cali', '40', print);
  conn.hset('HolbertonSchools', 'Paris', '2', print);
  conn.hgetall('HolbertonSchools', (err, res) => {
    if (err) {
      console.log(err.message);
      return;
    }
    console.log(res);
  });
});

import { createClient } from 'redis';

const conn = createClient();

conn.on('error', (err) => {
  console.log(
        `Redis client not connected to the server: ${err.message}`);
});

conn.on('connect', () => {
  console.log(
    'Redis client connected to the server');
});

conn.subscribe('holberton school channel');

conn.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    conn.unsubscribe();
    conn.quit();
  }
});
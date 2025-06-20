import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => (
  console.log(
    'Redis client connected to the server',
  )));

client.on('error', (err) => (
  console.log(
    `Redis client not connected to the server: ${err}`,
  )));

const channel = 'ALXchannel';
client.subscribe(channel);

client.on('message', (ch, msg) => {
  if (ch === channel) {
    console.log(msg);
    if (msg === 'KILL_SERVER') {
      client.unsubscribe(channel);
      client.quit();
    }
  }
});

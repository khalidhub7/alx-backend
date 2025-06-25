import kue from 'kue';
import redis from 'redis';
import express from 'express';
import { promisify } from 'util';

const client = redis.createClient();
const queue = kue.createQueue();
const app = express();

// make redis get/set support async/await
const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

// set initial seats in redis
(async () => {
  await setAsync('available_seats', 50);
})();
let reservationEnabled = true;

// get available seats
const getCurrentAvailableSeats = async () => {
  const value = await getAsync('available_seats');
  return Number(value);
};

// reserve seat
const reserveSeat = async (number) => {
  const openSeats = await getCurrentAvailableSeats();
  const seatsLeft = openSeats - number;
  if (seatsLeft < 0) {
    throw new Error('Not enough seats available');
  }
  if (seatsLeft === 0) { reservationEnabled = false; }
  await setAsync('available_seats', seatsLeft);
};

// api routes
app.get('/available_seats', async (_, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

app.get('/reserve_seat', (_, res) => {
  if (!reservationEnabled) {
    res.status(423).json({ status: 'Reservation are blocked' });
  } else {
    const job = queue.create('reserve_seat');
    job.save((err, __) => {
      if (err) {
        res.status(400).send({ status: 'Reservation failed' });
      } else {
        res.status(200).send({ status: 'Reservation in process' });
      }
    });

    job.on('complete', () => {
      console.log(`Seat reservation job ${job.id} completed`);
    });

    job.on('failed', (err) => {
      console.log(`Seat reservation job ${job.id} failed: ${err}`);
    });
  }
});

app.get('/process', (__, res) => {
  queue.process('reserve_seat', async (_, done) => {
    try {
      await reserveSeat(1); done();
    } catch (err) { done(err); }
  });
  res.json({ status: 'Queue processing' });
});
app.listen(1245, () => {
  console.log('server running on http://localhost:1245');
});

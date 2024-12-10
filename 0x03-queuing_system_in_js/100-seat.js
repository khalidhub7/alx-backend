import Redis from 'ioredis';
import kue from 'kue';
import express from 'express';

const redis = new Redis();
const queue = kue.createQueue();
const app = express();

let reservationEnabled = true;
async function initializeSeats () {
  await redis.set('available_seats', 50);
}

// retrieves available seats
async function getCurrentAvailableSeats () {
  const availableseats = await redis.get('available_seats');
  return Number(availableseats);
}

// reserves seats if available
async function reserveSeat (number) {
  const currentSeats = await getCurrentAvailableSeats();

  if (currentSeats === 0) {
    reservationEnabled = false;
    throw new Error('Not enough seats available');
  }

  if (currentSeats < number) {
    throw new Error(
      'Requested reservation exceeds available seats.');
  }
  await redis.set('available_seats', currentSeats - number);
}

// available seats route
app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

// reserves seats route
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat', { seats: 1 });

  job.save((err) => {
    if (!err) {
      return res.json({ status: 'Reservation in process' });
    }
    return res.status(500).json(
      { status: 'Reservation failed', error: err.message });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    console.log(
      `Seat reservation job ${job.id} failed: ${err.message}`);
  });
});

// process route to apply reservation
app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    try {
      await reserveSeat(job.data.seats);
      done();
    } catch (err) {
      done(err);
    }
  });
});

app.listen(1245, async () => {
  await initializeSeats();
  console.log('Server running at http://localhost:1245');
});

/* test

npm run dev 100-seat.js
curl localhost:1245/available_seats ; echo ""
curl localhost:1245/reserve_seat ; echo ""
curl localhost:1245/process ; echo ""
curl localhost:1245/available_seats ; echo ""
for n in {1..50}; do curl localhost:1245/reserve_seat ; echo ""; done
*/

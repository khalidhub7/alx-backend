import Kue from 'kue';

const jobData = {
  phoneNumber: '06xxxxxxxx',
  message: 'this is the notification msg message',
};

const queue = Kue.createQueue();

const job = queue.create('push_notification_code', jobData);

job.save((err) => {
  if (!err) { console.log(`Notification job created: ${job.id}`); }
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});

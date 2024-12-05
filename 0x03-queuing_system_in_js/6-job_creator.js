import kue from 'kue';

const queue = kue.createQueue();

const jobb = queue.create('push_notification_code', {
  phoneNumber: '06 xx 3x xx 71',
  message: 'test'
});

jobb.save((err) => {
  if (!err) {
    console.log(
            `Notification job created: ${jobb.id}`);
  }
});

jobb.on('failed', () => {
  console.log(
    'Notification job failed');
});

jobb.on('complete', () => {
  console.log(
    'Notification job completed');
});


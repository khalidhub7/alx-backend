import Kue from 'kue';

const queue = Kue.createQueue();

const sendNotification = (phoneNumber, message) => {
  if (phoneNumber && message) {
    console.log(`Sending notification \
to ${phoneNumber}, with message: ${message}`);
  }
};

queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});

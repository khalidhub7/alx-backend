const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  jobs.forEach((obj) => {
    const job = queue.create('push_notification_code_3', obj);
    job.save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    });

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });
    job.on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });
    job.on('progress', (percent) => {
      console.log(`Notification job ${job.id} ${percent}% complete`);
    });
  });
};
export default createPushNotificationsJobs;

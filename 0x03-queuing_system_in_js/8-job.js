
function createPushNotificationsJobs (jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw Error('Jobs is not an array');
  }

  for (const job of jobs) {
    const jobb = queue.create(
      'push_notification_code_3', job);

    jobb.save((err) => {
      if (!err) {
        console.log(
`Notification job created: ${jobb.id}`);
      }
    });

    jobb.on('failed', (err) => {
      console.log(
`Notification job ${jobb.id} failed: ${err.message}`);
    });

    jobb.on('progress', (percentage) => {
      console.log(
`Notification job ${jobb.id} ${percentage}% complete`);
    });
    jobb.on('complete', () => {
      console.log(
`Notification job ${jobb.id} completed`);
    });
  }
}

module.exports = createPushNotificationsJobs;

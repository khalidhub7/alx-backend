import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

const jobs = [
  { phoneNumber: '1234567890', message: 'Hello 1' },
  { phoneNumber: '2345678901', message: 'Hello 2' },
  { phoneNumber: '3456789012', message: 'Hello 3' },
];
const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });

  it('should throw err if jobs is not arr of objs', () => {
    expect(
      () => createPushNotificationsJobs({}, queue),
    ).throws(Error);
  });
  it('should add 3 jobs to queue', () => {
    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(3);

    queue.testMode.jobs.forEach((job) => {
      expect(job.type).to.equal('push_notification_code_3');
    });
  });

  afterEach(() => { queue.testMode.clear(); });
  after(() => { queue.testMode.exit(); });
});

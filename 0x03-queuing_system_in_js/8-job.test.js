import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  let queue;
  before(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it(
    'should throw an error if jobs is not an array', () => {
      expect(() => {
        createPushNotificationsJobs({}, queue).to.throw(
          'Jobs is not an array');
      });
    });

  it(
    'should add jobs to the queue correctly', () => {
      const jobs = [
        {
          phoneNumber: '4153518780',
          message: 'This is the code 1234 to verify your account'
        },
        {
          phoneNumber: '4153518781',
          message: 'This is the code 4562 to verify your account'
        },
        {
          phoneNumber: '4153518743',
          message: 'This is the code 4321 to verify your account'
        },
        {
          phoneNumber: '4153538781',
          message: 'This is the code 4562 to verify your account'
        },
        {
          phoneNumber: '4153118782',
          message: 'This is the code 4321 to verify your account'
        },
        {
          phoneNumber: '4153718781',
          message: 'This is the code 4562 to verify your account'
        },
        {
          phoneNumber: '4159518782',
          message: 'This is the code 4321 to verify your account'
        },
        {
          phoneNumber: '4158718781',
          message: 'This is the code 4562 to verify your account'
        },
        {
          phoneNumber: '4153818782',
          message: 'This is the code 4321 to verify your account'
        },
        {
          phoneNumber: '4154318781',
          message: 'This is the code 4562 to verify your account'
        },
        {
          phoneNumber: '4151218782',
          message: 'This is the code 4321 to verify your account'
        }
      ];

      createPushNotificationsJobs(jobs, queue);

      expect(
        queue.testMode.jobs.length).to.equal(jobs.length);

      let index = 0;
      for (const testjob of queue.testMode.jobs) {
        expect(
          testjob.type).to.equal('push_notification_code_3');
        expect(
          testjob.data.phoneNumber).to.equal(jobs[index].phoneNumber);
        expect(
          testjob.data.message).to.equal(jobs[index].message);
        index = index + 1;
      }
    });
});

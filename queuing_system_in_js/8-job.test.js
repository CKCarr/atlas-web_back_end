import createPushNotificationsJobs from './8-job.js';
import { createQueue } from 'kue';
import { expect } from 'chai';

describe('createPushNotificationsJobs Functionality', () => {
  let queue;

  before(() => {
    queue = createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  const listWithTwoJobs = [
    { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
    { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' }
  ];

  describe('Input Validation', () => {
    it('throws an error if jobs is not an array', () => {
      const invalidInputs = [{}, "string", 42];
      invalidInputs.forEach(input => {
        expect(() => createPushNotificationsJobs(input, queue)).to.throw(Error, 'Jobs parameter must be an array');
      });
    });
  });

  describe('Job Creation', () => {
    it('creates a job for each element in the array', () => {
      createPushNotificationsJobs(listWithTwoJobs, queue);
      expect(queue.testMode.jobs.length).to.equal(2);
    });

    it('creates a job with the correct type', () => {
      createPushNotificationsJobs(listWithTwoJobs, queue);
      expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    });

    it('creates a job with the correct data', () => {
      createPushNotificationsJobs(listWithTwoJobs, queue);
      expect(queue.testMode.jobs[0].data).to.deep.equal(listWithTwoJobs[0]);
    });
  });
});


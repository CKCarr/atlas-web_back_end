// 5-payment.test.js

const sinon = require('sinon');
const assert = require('assert');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi with hooks', function() {
  let consoleSpy;

  // Hook to set up before each test
  beforeEach(function() {
    consoleSpy = sinon.spy(console, 'log');
  });

  // Hook to tear down after each test
  afterEach(function() {
    consoleSpy.restore();
  });

  it('should log "The total is: 120" when called with 100 and 20', function() {
    sendPaymentRequestToApi(100, 20);
    assert(consoleSpy.calledWith('The total is: 120'), 'The console was not called with the expected string');
    assert(consoleSpy.calledOnce, 'The console should be called exactly once');
  });

  it('should log "The total is: 20" when called with 10 and 10', function() {
    sendPaymentRequestToApi(10, 10);
    assert(consoleSpy.calledWith('The total is: 20'), 'The console was not called with the expected string');
    assert(consoleSpy.calledOnce, 'The console should be called exactly once');
  });
});

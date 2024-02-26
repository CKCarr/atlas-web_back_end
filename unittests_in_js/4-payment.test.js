// 4-payment.test.js

const sinon = require('sinon');
const assert = require('assert');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi with stub', function() {
  it('should call calculateNumber stub and log correct message', function() {
    // Stubbing Utils.calculateNumber to always return 10
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
    // Spying on console.log to verify the output
    const logSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    // Verifying that the stub was called with expected arguments
    assert(stub.calledWith('SUM', 100, 20));
    // Verifying that console.log was called with the expected message
    assert(logSpy.calledWith('The total is: 10'));

    // Restore the stub and the spy
    stub.restore();
    logSpy.restore();
  });
});

// api.test.js

const chai = require('chai');
const request = require('request');
const expect = chai.expect;

describe('8-api test suite - Index page', function() {
  // Base URL of the server
  const baseURL = 'http://localhost:7865';

  // Test case for verifying the status code
  it('should return status code 200', function(done) {
    request.get(`${baseURL}/`, function(err, res, body) {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  // Test case for verifying the response body content
  it('should return the correct message', function(done) {
    request.get(`${baseURL}/`, function(err, res, body) {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});


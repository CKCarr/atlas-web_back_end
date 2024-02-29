// api.test.js

const chai = require('chai');
const request = require('request');
const expect = chai.expect;

describe('Index page', function() {
  const baseURL = 'http://localhost:7865';

  it('should return status code 200', function(done) {
    request.get(`${baseURL}/`, function(err, res, body) {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct message', function(done) {
    request.get(`${baseURL}/`, function(err, res, body) {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('Cart page', function() {
  const baseURL = 'http://localhost:7865';

  it('should return status code 200 for numeric id', function(done) {
    request.get(`${baseURL}/cart/12`, function(err, res, body) {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('should return status code 404 for non-numeric id', function(done) {
    request.get(`${baseURL}/cart/hello`, function(err, res, body) {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});


// api.test.js

const chai = require('chai');
const chaiHttp = require('chai-http');
const app = require('./api'); // Import the Express app
const { expect } = chai;

chai.use(chaiHttp);

describe('Index page', function() {
  // Test for the correct status code
  it('should return status code 200', function(done) {
    chai.request(app)
      .get('/')
      .end((err, res) => {
        expect(res).to.have.status(200);
        done();
      });
  });

  // Test for the correct result
  it('should return the correct message', function(done) {
    chai.request(app)
      .get('/')
      .end((err, res) => {
        expect(res.text).to.equal('Welcome to the payment system');
        done();
      });
  });
});

// test suite for the cart page
describe('Cart page', function() {
  // Correct status code when :id is a number
  it('should return status code 200 for numeric id', function(done) {
    chai.request(app)
      .get('/cart/12')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.text).to.equal('Payment methods for cart 12');
        done();
      });
  });

  // Correct status code when :id is NOT a number (=> 404)
  it('should return status code 404 for non-numeric id', function(done) {
    chai.request(app)
      .get('/cart/hello')
      .end((err, res) => {
        expect(res).to.have.status(404);
        done();
      });
  });
});

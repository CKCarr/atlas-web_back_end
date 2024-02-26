// 6-payment_token.test.js

const assert = require('assert');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function() {
  it('should return a resolved promise with the correct data when success is true', function(done) {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        assert.strictEqual(response.data, 'Successful response from the API');
        // Indicate that the test is complete
        done();
      })
      .catch((error) => done(error));
  });
});

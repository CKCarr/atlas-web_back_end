/* Create a new file named 3-payment.js:

Create a new function named sendPaymentRequestToApi.
 The function takes two argument totalAmount, and totalShipping
The function calls the Utils.calculateNumber function with type SUM,
totalAmount as a, totalShipping as b and
 display in the console the message The total is: <result of the sum> */
const Utils = require('./utils');

function sendPaymentRequestApi(totalAmount, totalShipping) {
    const sum = Utils.calculateNumber('SUM', totalAmount, totalShipping);
    console.log(`The total is: ${sum}`);
}

module.exports = sendPaymentRequestApi;

/* file 0-calcul.test.js that contains test cases of this function
You can assume a and b are always number
Tests should be around the “rounded” part */

/* eslint-disable jest/prefer-expect-assertions */
/* eslint-disable jest/expect-expect */
const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {

  it('test both positive integers - calculation', function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(1, 3.7), 5);
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('test both negative integers - calculation', () => {
    assert.strictEqual(calculateNumber(-1, -3), -4);
    assert.strictEqual(calculateNumber(-1, -3.7), -5);
    assert.strictEqual(calculateNumber(-1.2, -3.7), -5);
    assert.strictEqual(calculateNumber(-1.6, -3.7), -6);
  });

  it('test if a or b is not a number to return NaN', () => {
    assert.strictEqual(calculateNumber('A', 1.6), NaN);
    assert.strictEqual(calculateNumber(1.6, 'B'), NaN);
    assert.strictEqual(calculateNumber('A', 'B'), NaN);
  });

  it('test if a or b is infinite to return NaN', () => {
    assert.strictEqual(calculateNumber(Infinity, 1.6), Infinity);
    assert.strictEqual(calculateNumber(Infinity, Infinity), Infinity);
    assert.strictEqual(calculateNumber(-Infinity, 1.6), -Infinity);
    assert.strictEqual(calculateNumber(-Infinity, -Infinity), -Infinity);
    assert.strictEqual(calculateNumber(Infinity, -1.6), Infinity)
  });

  it('should handle cases where one or both numbers are negative', () => {
    assert.strictEqual(calculateNumber(-1, 3), 2);
    assert.strictEqual(calculateNumber(-1.5, -2.5), -3);
  });

  it('should handle cases with 0 correctly', () => {
    assert.strictEqual(calculateNumber(0, 0), 0);
    assert.strictEqual(calculateNumber(0, 3.7), 4);
  });

});

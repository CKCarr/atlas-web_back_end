/* file 0-calcul.test.js that contains test cases of this function
You can assume a and b are always number
Tests should be around the “rounded” part */

/* eslint-disable jest/prefer-expect-assertions */
/* eslint-disable jest/expect-expect */
const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {

  describe('SUM', () => {
    it('should sum two numbers after rounding', () => {
      assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
      assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
      assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
      assert.strictEqual(calculateNumber('SUM', 1.5, 3.7), 6);
    });

    it('should handle positive + negative correctly', () => {
    assert.strictEqual(calculateNumber('SUM', 5, -3), 2);
    });

    it('should handle cases with 0 correctly', () => {
    assert.strictEqual(calculateNumber('SUM', 0, 0), 0);
    assert.strictEqual(calculateNumber('SUM', 0, 3.7), 4);
    });
  });

  describe('SUBTRACT', () => {
    it('should subtract two numbers after rounding', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 1, 3), -2);
      assert.strictEqual(calculateNumber('SUBTRACT', 1, 3.7), -3);
      assert.strictEqual(calculateNumber('SUBTRACT', 1.2, 3.7), -3);
      assert.strictEqual(calculateNumber('SUBTRACT', 1.5, 3.7), -2);
    });

    it('should handle negative - positive correctly', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', -5, 3), -8);
    });

    it('should handle cases with 0 correctly', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 4, 0), 4);
    });
  });

  describe('DIVIDE', () => {
    it('should divide two numbers after rounding', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
      assert.strictEqual(calculateNumber('DIVIDE', 9, 2), 4.5);
    });

    it('should return "Error" when attempting to divide by 0', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });



    it('should handle negative / positive correctly', () => {
    assert.strictEqual(calculateNumber('DIVIDE', -9, 3), -3);
    });

    it('should handle positive / negative correctly', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 9, -3), -3);
    });

    it('should return "Error" when attempting to divide by 0', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 3.7, 0), 'Error');
    });
  });

});

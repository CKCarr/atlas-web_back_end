/* file 0-calcul.test.js that contains test cases of this function
You can assume a and b are always number
Tests should be around the “rounded” part */
const assert = require("assert");
const calculateNumber = require("./0-calcul.js");

describe('calculateNumber', () => {

  it('it round the first argument', () => {
    assert.equal(calculateNumber(1.0, 0), 1);
    assert.equal(calculateNumber(1.3, 0), 1);
    assert.equal(calculateNumber(1.7, 0), 2);
  });

  it('it round the second argument', () => {
    assert.equal(calculateNumber(0, 1.0), 1);
    assert.equal(calculateNumber(0, 1.3), 1);
    assert.equal(calculateNumber(0, 1.7), 2);
  });

  it('it should return the right number', () => {
    assert.equal(calculateNumber(1.3, 0), 1);
    assert.equal(calculateNumber(0, 1.2), 1);
    assert.equal(calculateNumber(1.3, 1.3), 2);
    assert.equal(calculateNumber(1.7, 1.2), 3);
    assert.equal(calculateNumber(1.3, 1.8), 3);
    assert.equal(calculateNumber(1.6, 1.8), 4);
  });

  it('return correctly with positive integers', function () {
    assert.equal(calculateNumber(1, 3), 4);
    assert.equal(calculateNumber(1, 3.8), 5);
    assert.equal(calculateNumber(1.4, 3.8), 5);
    assert.equal(calculateNumber(1.6, 3.8), 6);
    assert.equal(calculateNumber(3.8, 1), 5);
    assert.equal(calculateNumber(3.7, 1.2), 5);
  });

  it('returns correctly with negative integers', () => {
    assert.equal(calculateNumber(-1, -3), -4);
    assert.equal(calculateNumber(-1, -3.7), -5);
    assert.equal(calculateNumber(-1.2, -3.7), -5);
    assert.equal(calculateNumber(-1.6, -3.7), -6);
    assert.equal(calculateNumber(-3.7, -1), -5);
    assert.equal(calculateNumber(-3.7, -1.2), -5);
  });

  it('correctly sums two rounded numbers', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(1, 3.7), 5);
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('handles rounding up and down correctly', () => {
    assert.strictEqual(calculateNumber(1.4, 3.6), 5); // Rounds down then up
    assert.strictEqual(calculateNumber(1.5, 2.4), 4); // Rounds up then down
  });

});

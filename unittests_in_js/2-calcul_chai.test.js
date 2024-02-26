/* file 0-calcul.test.js that contains test cases of this function
You can assume a and b are always number
Tests should be around the “rounded” part */

/* eslint-disable jest/prefer-expect-assertions */
/* eslint-disable jest/expect-expect */
const expect = require('chai').expect;
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {

  describe('SUM', () => {
    it('should sum two numbers after rounding', () => {
      expect(calculateNumber('SUM', 1, 3)).to.equal(4);
      expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
      expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
      expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
    });

    it('should handle positive + negative correctly', () => {
    expect(calculateNumber('SUM', 5, -3)).to.equal(2);
    });

    it('should handle cases with 0 correctly', () => {
    expect(calculateNumber('SUM', 0, 0)).to.equal(0);
    expect(calculateNumber('SUM', 0, 3.7)).to.equal(4);
    });
  });

  describe('SUBTRACT', () => {
    it('should subtract two numbers after rounding', () => {
      expect(calculateNumber('SUBTRACT', 1, 3)).to.equal(-2);
      expect(calculateNumber('SUBTRACT', 1, 3.7)).to.equal(-3);
      expect(calculateNumber('SUBTRACT', 1.2, 3.7)).to.equal(-3);
      expect(calculateNumber('SUBTRACT', 1.5, 3.7)).to.equal(-2);
    });

    it('should handle negative - positive correctly', () => {
    expect(calculateNumber('SUBTRACT', -5, 3)).to.equal(-8);
    });

    it('should handle cases with 0 correctly', () => {
    expect(calculateNumber('SUBTRACT', 4, 0)).to.equal(4);
    });
  });

  describe('DIVIDE', () => {
    it('should divide two numbers after rounding', () => {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
      expect(calculateNumber('DIVIDE', 9, 2)).to.equal(4.5);
    });

    it('should return "Error" when attempting to divide by 0', () => {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });



    it('should handle negative / positive correctly', () => {
      expect(calculateNumber('DIVIDE', -9, 3)).to.equal(-3);
    });

    it('should handle positive / negative correctly', () => {
      expect(calculateNumber('DIVIDE', 9, -3)).to.equal(-3);
    });

    it('should return "Error" when attempting to divide by 0', () => {
      expect(calculateNumber('DIVIDE', 3.7, 0)).to.equal('Error');
    });
  });

});

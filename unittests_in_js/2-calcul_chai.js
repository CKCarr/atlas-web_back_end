/* file named 0-calcul.js:

Create a function named calculateNumber.
It should accepts two arguments (number) a and b
The function should round a and b and return the sum of it */

function calculateNumber(type, a, b) {
    const roundedA = Math.round(a)
    const roundedB = Math.round(b);

    switch (type) {
        case 'SUM':
            return roundedA + roundedB;
        case 'SUBTRACT':
            return roundedA - roundedB;
        case 'DIVIDE':
            if (roundedB === 0) return 'Error';
            return roundedA / roundedB;
        default:
            return 'Invalid operation';
    }
}

module.exports = calculateNumber;

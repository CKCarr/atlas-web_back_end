// api.js

const express = require('express');
const app = express();

app.get('/', (request, response) => {
    response.send('Welcome to the payment system');
});

// New endpoint for cart eith numeric ID validation
app.get('/cart/:id(\\d+)', (request, response) => {
    const id = request.params.id;
    response.send(`Payment methods for cart ${id}`);
});

const PORT = 7865;
app.listen(PORT, ()=> {
    console.log(`API availabile on localhost port ${PORT}`);
});

module.exports = app;

// api.js

const express = require('express');
const app = express();

app.get('/', (request, response) => {
    response.send('Welcome to the payment system');
});

const PORT = 7865;
app.listen(PORT, ()=> {
    console.log(`API availabile on localhost port ${PORT}`);
});

module.exports = app;

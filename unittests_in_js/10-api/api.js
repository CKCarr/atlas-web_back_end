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

// New /available_payments endpoint
app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  });
});

// express
app.use(express.json())

// New /login endpoint
app.post('/login', (req, res) => {
  const { userName } = req.body;
  res.send(`Welcome ${userName}`);
});

const PORT = 7865;
app.listen(PORT, ()=> {
    console.log(`API availabile on localhost port ${PORT}`);
});

module.exports = app;

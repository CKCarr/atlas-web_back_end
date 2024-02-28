import redis from 'redis';
import express from 'express';
import { promisify } from 'util';

const app = express();
const PORT = 1245;
const client = redis.createClient();

// Error handling for Redis client
client.on('error', (error) => {
  console.error(`Redis error: ${error}`);
});

// Promisify Redis client methods
const asyncSet = promisify(client.set).bind(client);
const asyncGet = promisify(client.get).bind(client);

const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50, initialAvailableQuantity: 4
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100, initialAvailableQuantity: 10
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350, initialAvailableQuantity: 2
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550, initialAvailableQuantity: 5
  }
]

// Initialize Redis with product stock
const initializeProductStock = () => {
  listProducts.forEach(async (product) => {
    await asyncSet(`item.${product.itemId}`, product.initialAvailableQuantity);
  });
};

// Function to get an item by its ID
const getItemById = (id) => {
  return listProducts.find((item) => item.itemId === parseInt(id, 10));
};

// Endpoint to list all products
app.get('/list_products', (req, res) => {
  res.send(listProducts);
});

// Function to reserve stock by item ID
const reserveStockById = async (itemId, stock) => {
  await asyncSet(`item.${itemId}`, stock);
};

// Function to get stock by item ID
const getStockById = async (itemId) => {
  const stock = await asyncGet(`item.${itemId}`);
  return parseInt(stock, 10);
};

// Endpoint to get a product by its ID
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(itemId);

  if (item) {
    const stock = await getStockById(itemId);
    const itemWithStock = { ...item, initialAvailableQuantity: stock };
    res.send(itemWithStock);
  } else {
    res.status(404).send({ status: 'Product not found' });
  }
});


// Endpoint to reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(itemId);

  if (!item) {
    res.status(404).send({ status: 'Product not found' });
    return;
  }

  const stock = await getStockById(itemId);
  if (stock > 0) {
    await reserveStockById(itemId, stock - 1);
    res.send({ status: "Reservation confirmed", itemId: itemId });
  } else {
    res.status(404).send({ status: 'Product not available' });
  }
});

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
  initializeProductStock();
});

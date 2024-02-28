// Import the redis client using ES6 syntax
import redis from 'redis';

// Create a client instance
const client = redis.createClient({
  host: 'localhost',
  port: 6379
});

// Listen for the "connect" event to log the successful connection
client.on('connect', function() {
    console.log('Redis client connected to the server');
});

// Listen for the "error" event to log any errors
client.on('error', function(error) {
    console.log(`Redis client not connected to the server: ${error.message}`);
});


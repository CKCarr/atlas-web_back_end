// full_server/server.js
import express from 'express';

const routes = require('./routes/index');

const app = express();

app.use(routes);

const PORT = 1245;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

export default app;

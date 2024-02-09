# NoSQL

## Learning Objectives

## What is NoSQL?
NoSQL stands for "Not Only SQL." It refers to a wide range of database technologies that were developed to handle large volumes of data, rapid scaling, and the ability to manage types of data (structured, semi-structured, and unstructured) that don't fit neatly into the rows and columns of traditional relational databases (RDBMS). NoSQL databases are designed for specific data models and have flexible schemas for building modern applications.

### Difference Between SQL and NoSQL
- Data Structure: SQL databases are table-based, while NoSQL databases can be document-oriented, key-value pairs, wide-column stores, or graph databases.
- Schema Flexibility: NoSQL provides more flexibility with data models, whereas SQL requires a predefined schema.
- Scaling: SQL databases are typically scaled by enhancing the horse-power of the hardware (vertical scaling), whereas NoSQL databases are scaled across many systems (horizontal scaling).
- Use Cases: SQL is preferred for complex queries and transactional applications requiring ACID compliance. NoSQL is chosen for rapid development, high scalability, and for handling large volumes of data and unstructured data.
### What is ACID?
ACID stands for Atomicity, Consistency, Isolation, Durability. It's a set of properties that guarantee database transactions are processed reliably:

- Atomicity: Each transaction is fully completed or fully failed.
- Consistency: Data must meet all validation rules.
- Isolation: Transactions are processed independently.
- Durability: Once a transaction is committed, it will remain so.
### Document Storage
Document storage is a type of NoSQL database that stores data as documents, which can be JSON, BSON (Binary JSON), XML, or other formats. MongoDB is a popular example, where each document is unique and has its own structure.

### NoSQL Types
- Document Databases: Stores data in documents (e.g., MongoDB).
- Key-Value Stores: Stores data as key-value pairs (e.g., Redis).
- Wide-Column Stores: Stores data in tables, rows, and dynamic columns (e.g., Cassandra).
- Graph Databases: Stores data in nodes and relationships (e.g., Neo4j).
Benefits of NoSQL Database
- Scalability: Easily scales horizontally.
- Flexibility: Can store different types of data together.
- Speed: Optimized for specific data models and access patterns.
- Development Speed: Flexible schema allows for quicker iteration.
### Querying NoSQL Databases

Querying in NoSQL databases varies depending on the type. In MongoDB, you can query data using methods like find() for retrieving documents, aggregate() for complex data aggregation, and more.

- Insert/Update/Delete in MongoDB
- Insert: db.collection.insertOne() or db.collection.insertMany().
- Update: db.collection.updateOne(), db.collection.updateMany(), or db.collection.replaceOne().
- Delete: db.collection.deleteOne() or db.collection.deleteMany().
### Aggregation
Aggregation in MongoDB processes data records and returns computed results. Aggregation operations group values from multiple documents together and can perform a variety of operations on the grouped data to return a single result.

### MongoDB and Python
MongoDB can be used with Python through the pymongo library. Here's an example of connecting to a MongoDB database and inserting a document:

```python

from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Select the database
db = client.mydatabase

# Select the collection
collection = db.mycollection

# Insert a document
collection.insert_one({"name": "John Doe", "age": 30})
```
### Mongo Shell Methods
The mongo shell is an interactive JavaScript interface to MongoDB. You can perform database operations with JavaScript functions and commands. For instance, to find documents in a collection, you would use:

``` javascript

db.collection.find({ "name": "John Doe" })
```

The mongo Shell
The mongo shell is a powerful tool for interacting with MongoDB directly. It allows you to query and update data, manage the database structure, and perform administrative tasks.

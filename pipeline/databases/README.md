# Database Basics README

## What's a Relational Database?

A relational database is a type of database that stores and organizes data in tables with rows and columns. It uses a structured query language (SQL) for defining, manipulating, and querying data. The data in a relational database is typically organized to enforce relationships between different tables.

## What's a Non-Relational Database?

A non-relational database, often referred to as NoSQL (Not Only SQL), is a type of database that does not rely on the traditional tabular format seen in relational databases. NoSQL databases are designed to handle large volumes of unstructured or semi-structured data and offer more flexibility in data modeling compared to relational databases.

## Difference Between SQL and NoSQL

The main difference between SQL and NoSQL databases lies in their data model and querying language. SQL databases follow a structured schema with predefined tables and relationships, while NoSQL databases offer a more flexible schema and use various data models such as document, key-value, columnar, or graph. Additionally, SQL databases use SQL for querying, whereas NoSQL databases use different query languages or APIs depending on the specific type.

## How to Create Tables with Constraints

In SQL, you can create tables with constraints to enforce data integrity and maintain consistency. Constraints include primary keys, foreign keys, unique constraints, check constraints, and not null constraints. Here's a basic example of creating a table with constraints:

```sql
CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    Username VARCHAR(50) UNIQUE,
    Email VARCHAR(100) NOT NULL,
    Password VARCHAR(50) CHECK (LENGTH(Password) >= 8)
);
```

## How to Optimize Queries by Adding Indexes

Indexes are used to optimize query performance by allowing faster data retrieval. You can add indexes to columns frequently used in WHERE clauses, JOIN conditions, or ORDER BY clauses. Here's how to add an index to a column:

```sql
CREATE INDEX idx_username ON Users(Username);
```

## What Is and How to Implement Stored Procedures and Functions in MySQL

Stored procedures and functions are reusable sets of SQL statements stored in the database and executed by calling their name. They help improve code reusability, maintainability, and security. Here's how to create a simple stored procedure in MySQL:

```sql
DELIMITER //

CREATE PROCEDURE GetUserInfo (IN userId INT)
BEGIN
    SELECT * FROM Users WHERE UserID = userId;
END //

DELIMITER ;
```

## What Is and How to Implement Views in MySQL

A view in MySQL is a virtual table generated by a query. It represents a subset of data from one or more tables and can simplify complex queries. Here's how to create a view:

```sql
CREATE VIEW ActiveUsers AS
SELECT * FROM Users WHERE IsActive = 1;
```

## What Is and How to Implement Triggers in MySQL

Triggers in MySQL are stored procedures that are automatically executed or fired when certain events occur in the database. These events include INSERT, UPDATE, or DELETE operations on specific tables. Here's how to create a trigger:

```sql
CREATE TRIGGER AuditLog AFTER INSERT ON Users
FOR EACH ROW
INSERT INTO AuditTrail (Action, UserID) VALUES ('INSERT', NEW.UserID);
```

## What Is ACID

ACID is an acronym that stands for Atomicity, Consistency, Isolation, and Durability. It is a set of properties that guarantee reliability and integrity in database transactions:

- **Atomicity**: Ensures that transactions are treated as a single unit of work, either fully completed or fully rolled back.
- **Consistency**: Ensures that the database remains in a consistent state before and after the transaction.
- **Isolation**: Ensures that transactions are executed independently and do not interfere with each other.
- **Durability**: Ensures that once a transaction is committed, its changes are permanent and survive system failures.

## What Is Document Storage

Document storage is a type of storage model used in NoSQL databases where data is stored as flexible, self-describing documents, typically in JSON or BSON format. Each document can have its own unique structure, making it suitable for storing semi-structured or unstructured data.

## What Are NoSQL Types

NoSQL databases are categorized into different types based on their data model:

1. **Document databases**: Store data as documents, e.g., MongoDB.
2. **Key-value stores**: Store data as key-value pairs, e.g., Redis.
3. **Column-family stores**: Store data in columns rather than rows, e.g., Apache Cassandra.
4. **Graph databases**: Store data in graph structures with nodes, edges, and properties, e.g., Neo4j.

## Benefits of a NoSQL Database

NoSQL databases offer several advantages over traditional SQL databases:

- **Scalability**: NoSQL databases can easily scale horizontally to handle large volumes of data and high throughput.
- **Flexibility**: NoSQL databases allow for flexible data modeling and schema evolution.
- **Performance**: NoSQL databases often provide high performance for specific use cases, such as real-time analytics or content management.
- **Fault tolerance**: Many NoSQL databases offer built-in fault tolerance and high availability features.

## How to Query Information from a NoSQL Database

Querying information from a NoSQL database depends on the specific database type and its query language or API. For example, in MongoDB, you can query data using the `find()` method:

```javascript
db.collection.find({ key: value });
```

## How to Insert/Update/Delete Information from a NoSQL Database

Inserting, updating, and deleting information from a NoSQL database also varies based on the database type and its API. In MongoDB, you can use methods like `insertOne()`, `updateOne()`, and `deleteOne()`:

```javascript
db.collection.insertOne({ key: value });
db.collection.updateOne({ key: value }, { $set: { key: newValue } });
db.collection.deleteOne({ key: value });
```

## How to Use MongoDB

MongoDB is a popular document-oriented NoSQL database. To use MongoDB, you need to install it on your system, start the MongoDB server, and then interact with it using the MongoDB shell or drivers for your programming language. Here's a basic example of using MongoDB shell:

```bash
# Start MongoDB server
mongod

# Start MongoDB shell
mongo

# Insert document into collection
> db.users.insertOne({ name: "John Doe", age: 30 })

# Query documents from collection
> db.users.find()
```
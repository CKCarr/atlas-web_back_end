# MySQL advanced
For this project, we expect you to look at this concept:

## Advanced SQL

Resources
Read or watch:

[MySQL cheatsheet]()
[MySQL Performance: How To Leverage MySQL Database Indexing]()
[Stored Procedure]()
[Triggers]()
[Views]()
[Functions and Operators]()
[Trigger Syntax and Examples]()
[CREATE TABLE Statement]()
[CREATE PROCEDURE and CREATE FUNCTION Statements]()
[CREATE INDEX Statement]()
[CREATE VIEW Statement]()


##Learning Objectives
General
- How to create tables with constraints
- How to optimize queries by adding indexes
- What is and how to implement stored procedures and functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL
## Requirements
General
- All your files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc
## More Info
    -Comments for your SQL file:
~~~
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
~~~

 ## Use “container-on-demand” to run MySQL

- Ask for container Ubuntu 18.04 - Python 3.7
- Connect via SSH
- Or via the WebTerminal
- In the container, you should start MySQL before playing with it:
~~~
$ service mysql start
 * MySQL Community Server 5.7.30 is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password:
Database
information_schema
mysql
performance_schema
sys
$
~~~
In the container, credentials are root/root

## How to import a SQL dump
The initial part of your request involves importing a SQL dump into a MySQL database, which is a common task when setting up databases or transferring data. The rest of the tasks involve various SQL operations, including creating tables, indexes, triggers, stored procedures, and functions.
### Importing a SQL Dump
Create the database if it doesn't already exist:

~~~ sh

echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
~~~
Import the SQL dump. The curl command fetches the SQL dump file, and the pipe | directs the output to the mysql command to import it into your database:

~~~ sh

curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
~~~
Verify the import by querying the database:

~~~sh

echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
~~~

# Using MySQL in a container 
Using a "container-on-demand" service to run MySQL can provide a flexible and isolated environment for your database operations. Here's a step-by-step guide on how you can set up and use MySQL in a container running Ubuntu 18.04 and Python 3.7:

## 1. Start the Container
Request a container with Ubuntu 18.04 and Python 3.7.
Once the container is ready, connect to it via SSH or the WebTerminal provided by the container platform.

## 2. Start MySQL Service
After connecting to the container, you'll need to start the MySQL service. You can do this by running the following command:

~~~sh

service mysql start
~~~
You should see a message indicating that MySQL Community Server 5.7.30 has started.

## 3. Interacting with MySQL
You can interact with MySQL using the mysql command-line tool. Since the credentials in the container are root/root, you won't need to enter a password if you're logging in as the root user.

- To execute SQL commands from a file (like 0-list_databases.sql), you can use the following syntax:

~~~sh

cat 0-list_databases.sql | mysql -uroot -p my_database
~~~
- When prompted for a password, enter 'root' (if it's set), or just press Enter if no password is set.

## 4. Common MySQL Commands in the Container
- Listing Databases: To list all databases, you can use the SQL file (as you've shown) or directly run:

~~~sh

echo "SHOW DATABASES;" | mysql -uroot -p
~~~
- Creating a Database: You can create a new database by running:

~~~ sh

echo "CREATE DATABASE my_new_database;" | mysql -uroot -p
~~~
- Selecting a Database: To start working with a specific database:

~~~sh

mysql -uroot -p -D my_database
~~~
- Running SQL Scripts: To run a SQL script from a file:

~~~sh

mysql -uroot -p my_database < my_script.sql
~~~
## Best Practices & Tips
- Security: Even if it's just a container, avoid using simple passwords like 'root/root'. If this container is accessible from the internet, it could be a security risk.
- Persistence: Remember that containers are ephemeral. If you stop your container, you might lose your database unless you're using a data volume to persist the data.
- Backups: Regularly backup your data, especially if you're using this setup for development and testing.

# SQL Tasks

Let's go through your tasks one by one:

### 0. We are all unique!
Create a users table with unique email addresses.
Use NOT NULL to prevent null values.
Set id as the primary key that auto-increments.
Use UNIQUE constraint for the email field to ensure all emails are unique.
### 1. In and not out
Similar to the previous task but add a country field.
Use ENUM for the country field to restrict it to specific values ('US', 'CO', 'TN').
### 2. Best band ever!
Import the metal_bands.sql dump.
Create a query that ranks country origins of bands based on the number of fans.
Use ORDER BY to sort the results.
### 3. Old school band
Use the metal_bands data.
Calculate the lifespan of bands (difference between formed and split).
Sort the result based on the lifespan.
### 4. Buy buy buy
Create a trigger that decreases the quantity of an item after adding a new order.
Use BEFORE INSERT or AFTER INSERT on the orders table to adjust the items table.
### 5. Email validation to sent
Create a trigger that resets the valid_email attribute when the email is changed.
Use BEFORE UPDATE on the users table.
### 6. Add bonus
Create a stored procedure AddBonus to add a new correction for a student.
Handle the creation of a new project if it doesn't exist.
Insert the score for the user in the correction.
### 7. Average score
Create a stored procedure ComputeAverageScoreForUser to compute and store the average score for a student.
Make sure to handle decimal values for the average.
### 8. Optimize simple search
Create an index on the first letter of the name field in the names table.
Use a prefix index to index only the first letter.
### 9. Optimize search and score
Create an index on the first letter of the name field and the score field in the names table.
Again, consider using a prefix index for the name field.
### 10. Safe divide
Create a function SafeDiv that safely divides two numbers and handles division by zero by returning 0.

## Best Practices & Tips
- Testing: Test each SQL script independently to ensure it works as expected.
- Comments: Add comments before your SQL queries to describe what each script does, following the guidelines you mentioned.
- Backup: Always backup your current database before running scripts that modify your data or structure.
- Version Control: Keep your SQL scripts in a version control system to track changes and collaborate with others.

.
├── 0-uniq_users.sql
├── 1-country_users.sql
├── 10-div.sql
├── 11-need_meeting.sql
├── 2-fans.sql
├── 3-glam_rock.sql
├── 4-store.sql
├── 5-valid_email.sql
├── 6-bonus.sql
├── 7-average_score.sql
├── 8-index_my_names.sql
├── 9-index_name_score.sql
├── Dockerfile
├── Makefile
└─ README.md

<hr>

#  Advanced SQL concepts using MySQL

## 1. Creating Tables with Constraints
When you create tables, constraints are rules you apply to the columns to ensure data integrity. Common constraints include:

- PRIMARY KEY: Uniquely identifies each record in a table.
- FOREIGN KEY: Ensures referential integrity by linking columns of multiple tables.
- NOT NULL: Ensures that a column cannot have a NULL value.
- UNIQUE: Ensures all values in a column are different.
- CHECK: Ensures the value in the column meets a specific condition.

Best Practice: Always define primary keys for your tables to ensure each record can be uniquely identified. Use foreign keys to maintain data integrity across related tables.

## 2. Optimizing Queries by Adding Indexes
Indexes are used to speed up the retrieval of rows from a table. Proper indexing can significantly improve the performance of your database.

Use the EXPLAIN statement before your SELECT queries to understand how MySQL will execute your query and whether it will use indexes.

Use the CREATE INDEX statement to add indexes to columns that are frequently used in the WHERE, ORDER BY, and JOIN conditions.

Best Practice: While indexes speed up querying, they slow down data insertion and modification. So, balance the number of indexes and only create them on columns that are frequently used in search conditions.

## 3. Stored Procedures and Functions
Stored Procedures and Functions are SQL statements that are stored in the database and can be executed whenever you need to perform the operation.

Stored Procedures: Perform a sequence of operations. They can have input/output parameters.

Functions: Perform operations and must return a value.

Best Practice: Use stored procedures and functions for operations that are performed frequently. This encapsulates logic in the database, promotes code reuse, and can improve performance.

## 4. Views in MySQL
Views are virtual tables that are based on the result-set of an SQL statement. They don't store data themselves but display data stored in other tables.

Use the CREATE VIEW statement to create a view.
Views can be used to simplify complex queries, ensure data security, and present data in a specific format.

Best Practice: Use views to abstract complexity and ensure users only have access to specific data in a controlled manner.

## 5. Triggers in MySQL
Triggers are database operations that are automatically performed when certain events occur.

Use triggers to enforce business rules, validate input data, and maintain audit logs.
Be cautious with triggers as they can make debugging more complex.

Best Practice: Ensure that triggers are used sparingly and only for operations that cannot be handled at the application level. Keep the logic within triggers simple and efficient.

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
The initial part of your request involves importing a SQL dump into a MySQL database, which is a common task when setting up databases or transferring data. The rest of the tasks involve various SQL operations, including creating tables, indexes, triggers, stored procedures, and functions. We'll go through each task and provide guidance and best practices.

Importing a SQL Dump
Create the database if it doesn't already exist:

~~~ sh

echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Import the SQL dump. The curl command fetches the SQL dump file, and the pipe | directs the output to the mysql command to import it into your database:

sh
Copy code
curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Verify the import by querying the database:

sh
Copy code
echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
~~~

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

 # Learning Objectives 

Examples of Personally Identifiable Information (PII)

How to implement a log filter that will obfuscate PII fields

How to encrypt a password and check the validity of an input password

How to authenticate to a database using environment variables

## What Is PII, non-PII, and Personal Data?

- PII (Personally Identifiable Information): Data that can be used to identify a specific individual. Examples include name, address, phone number, social security number, and email address.

- Non-PII: Information that cannot be used to identify an individual when viewed alone. Examples include browser types, device types, or demographic data not linked to individuals.

- Personal Data: A broader term used in data protection and privacy laws; it can include PII and any information relating to an identified or identifiable person.

## Logging Documentation

- Focus on understanding how logging works in your programming environment (e.g., Python, Java).
- Learn about log levels (debug, info, warning, error, critical) and how to configure them.
bcrypt Package

## bcrypt:
 is used for password hashing. 
 - Understand how to hash a password and how to check a hashed password against a plain text password to verify its validity.

## Logging to Files, Setting Levels, and Formatting

- Learn how to direct log output to files instead of the console.
- Understand how to set different logging levels for different outputs (e.g., debug level for file output, warning level for console).
- Familiarize yourself with log formatting to include useful information like timestamps, log levels, and messages.

## Implementing a Log Filter to Obfuscate PII Fields

- Understand how to create a custom log filter that can detect and obfuscate PII in log messages.
- This might involve using regular expressions or other methods to identify PII and replace it with placeholder text.

## How to Encrypt a Password and Check the Validity of an Input Password
- Learn how to use bcrypt or similar libraries to encrypt passwords.
- Understand the concept of salt and how it adds security to password hashing.
- Learn how to compare a hashed password with a plaintext password to authenticate users.

## How to Authenticate to a Database Using Environment Variables

- Understand the importance of not hardcoding credentials in your code.
- Learn how to use environment variables to securely store database credentials.
- Familiarize yourself with accessing these variables in your code for database connections.

Each of these areas is crucial for handling data securely and responsibly in software development. It's a combination of understanding the theory (like what constitutes PII) and practical skills (like using bcrypt for password hashing and setting up logging properly).

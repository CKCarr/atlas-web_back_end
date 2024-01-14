#!/usr/bin/env python3
""" filtered_logger Module

This module provides functionality for filtering and obfuscating
personal data from log messages.
It includes the filter_datum function,
which can be used to replace specific fields in a log message with a
redaction string, helping to ensure that sensitive information is not
exposed in log outputs.

Functions:
    filter_datum(fields: List[str],
    redaction: str, message: str, separator: str) -> str

Obfuscates specified fields in a log message.


class RedactingFormatter(logging.Formatter):
        Redacting Formatter class
        Inherits from logging.Formatter

"""

import re
from typing import List
import logging
import os
import mysql.connector
from mysql.connector import connection



PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """ function filter_datum
    Obfuscates specified fields in a log message.

    Args:
        fields: A list of strings representing all fields to obfuscate.
        redaction: A string representing by what the field will be obfuscated.
        message: A string representing the log line.
        separator: A string representing by which character fields
        in the log line are separated.

    Returns:
        The obfuscated log message.
    """
    for field in fields:
        message = re.sub(
            f"{field}=[^{separator}]+", f"{field}={redaction}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class

    Inherits from logging.Formatter

    creates variables for class RedactingFormatter
    REDACTION: A string representing by what the field will be obfuscated.
    FORMAT: A string representing the format of the log message.
    SEPARATOR: A string representing by which character fields
    in the log line are separated.

    functions:
        format(record: logging.LogRecord) -> List[str]
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ function __init__
        Constructor method for RedactingFormatter class

        Args:
            self: The object itself.
            fields (List[str]):  A list of strings representing all fields
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Function format
        Filters values in incoming log records using filter_datum.
        Args:
            record: A logging.LogRecord object.
        Returns:
            The obfuscated log message.
        """
        return filter_datum(
            fields=self.fields,
            redaction=self.REDACTION,
            message=super().format(record),
            separator=self.SEPARATOR)


def get_logger() -> logging.Logger:
    """ function get_logger
    takes no arguments and returns a logging.Logger object.

    Returns:
        A logging.Logger object.
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # create a Stream Handler with RedactingFormatter class as formatter
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=list(PII_FIELDS))
    stream_handler.setFormatter(formatter)

    # add Stream Handler to logger
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ function get_db

    Returns a connector to the database.

    Returns:
        mysql.connector.connection.MySQLConnection: _description_
    """
    db_user = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    try:
        return mysql.connector.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            database=db_name
        )
    except mysql.connector.Error as err:
        # if connection fails, log the error and exit
        logging.error(f"DB connection error: {err}")
        raise

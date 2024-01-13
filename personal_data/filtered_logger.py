#!/usr/bin/env python3
import re
from typing import List
"""
filtered_logger Module
----------------------

This module provides functionality for filtering and obfuscating
personal data from log messages. It includes the filter_datum function,
which can be used to replace specific fields in a log message with a
redaction string, helping to ensure that sensitive information is not
exposed in log outputs.

Functions:
    filter_datum(fields: List[str],
    redaction: str, message: str, separator: str) -> str
        Obfuscates specified fields in a log message.
"""


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """ Returns the log message obfuscated.

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

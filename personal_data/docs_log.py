# !/usr/bin/env python3

python3 -c 'print(__import__("filtered_logger").__doc__)'
python3 -c 'print(__import__("filtered_logger").RedactingFormatter.__doc__)'
python3 -c 'print(__import__("filtered_logger").RedactingFormatter.format.__doc__)'
python3 -c 'print(__import__("filtered_logger").filter_datum.__doc__)'
python3 -c 'print(__import__("filtered_logger").get_logger.__doc__)'

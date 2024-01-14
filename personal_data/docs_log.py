# !/usr/bin/env python3

# module doc filtered logger
python3 -c 'print(__import__("filtered_logger").__doc__)'
# class doc RedactingFormatter
python3 -c 'print(__import__("filtered_logger").RedactingFormatter.__doc__)'
# class doc RedactingFormatter function format doc
python3 -c 'print(__import__("filtered_logger").RedactingFormatter.format.__doc__)'
# function doc filter_datum
python3 -c 'print(__import__("filtered_logger").filter_datum.__doc__)'
# function doc get_logger
python3 -c 'print(__import__("filtered_logger").get_logger.__doc__)'
# function doc get_db
python3 -c 'print(__import__("filtered_logger").get_db.__doc__)'
# function doc main
python3 -c 'print(__import__("filtered_logger").main.__doc__)'

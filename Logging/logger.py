import logging

logging.basicConfig(level=logging.INFO, filename="logger.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")

# There are different levels of logging
# If a level is selected, then all the below that selected level, including that level, will be logged
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

# log variable
x = 10
logging.info(f"The value of x is {x}")

# log errors and exceptions
try:
    a = 10 / 0
except ZeroDivisionError as e:
    logging.error("Cannot divide by zero (by error)", exc_info=True)

try:
    a = 10 / 0
except ZeroDivisionError as e:
    logging.exception("Cannot divide by zero (by exception)")


# You can also create custom loggers, i.e., one logger for one module (eg: HTTP, EMAIL, etc)


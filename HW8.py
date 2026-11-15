import logging

logging.basicConfig(level=logging.ERROR, format="%(levelname)s: %(message)s")

try:
    result = 10 / 0
except ZeroDivisionError as e:
    logging.error(f"Сталася помилка: {e}")
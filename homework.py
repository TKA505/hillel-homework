import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

c_handler = logging.StreamHandler()
c_handler.setLevel(logging.INFO)

f_handler = logging.FileHandler("homework.log")
f_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
c_handler.setFormatter(formatter)
f_handler.setFormatter(formatter)

logger.addHandler(c_handler)
logger.addHandler(f_handler)


def divide(a, b):
    logger.debug(f"Виклик divide з аргументами: a={a}, b={b}")
    try:
        result = a / b
        logger.info(f"Результат ділення {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error(f"Спроба ділення на нуль: {a} / {b}")


if __name__ == "__main__":
    divide(10, 2)
    divide(10, 0)
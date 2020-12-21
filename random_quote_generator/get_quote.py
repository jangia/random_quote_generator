import random

from random_quote_generator.quotes import quotes


def get_quote() -> dict:
    """
    Get random quote
    :return:
    """

    return quotes[random.randint(0, len(quotes) - 1)]

from random_quote_generator.quotes import quotes
from random_quote_generator import get_quote


def test_get_quote():
    """
    GIVEN
    WHEN get_quote is called
    THEN random quote from quotes is returned
    """

    quote = get_quote()

    assert quote in quotes

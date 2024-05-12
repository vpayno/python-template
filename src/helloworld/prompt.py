"""
Writes text prompts.
"""


def words(message: str) -> str:
    r"""
    Generates the string message.
    """

    return message.rstrip()


def say(message: str) -> None:
    r"""
    Writes the message.
    """

    print(words(message))

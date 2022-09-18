#!/env/bin/python3
"""function that raises a name exception with a message."""


from logging import exception


def raise_exception_msg(message=""):
    raise NameError(message)

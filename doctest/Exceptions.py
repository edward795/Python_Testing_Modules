def add2num(x, y):
    """Adds two given numbers and returns the sum.
    >>> add2num(6, 7)
    13
    >>> add2num(-8.5, 7)
    -2.5
    >>> add2num(8, 'hello')
    Traceback (most recent call last):
    ValueError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return x + y
	
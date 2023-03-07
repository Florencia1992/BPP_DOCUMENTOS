def suma(x, y):
    """
    Returns the sum of two numbers.

    :param x: The first number.
    :type x: float or int
    :param y: The second number.
    :type y: float or int
    :return: The sum of the two numbers.
    :rtype: float or int
    """
    return x + y


def resta(x, y):
    """
    Returns the difference of two numbers.

    :param x: The first number.
    :type x: float or int
    :param y: The second number.
    :type y: float or int
    :return: The difference of the two numbers.
    :rtype: float or int
    """
    return x - y


def multiplica(x, y):
    """
    Returns the product of two numbers.

    :param x: The first number.
    :type x: float or int
    :param y: The second number.
    :type y: float or int
    :return: The product of the two numbers.
    :rtype: float or int
    """
    return x * y


def divide(x, y):
    """
    Returns the quotient of two numbers.

    :param x: The numerator.
    :type x: float or int
    :param y: The denominator.
    :type y: float or int
    :raises ZeroDivisionError: If the denominator is zero.
    :return: The quotient of the two numbers.
    :rtype: float or int
    """
    if y == 0:
        raise ZeroDivisionError('division by zero')
    return x / y






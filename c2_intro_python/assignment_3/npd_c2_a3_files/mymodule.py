def add_intergers(n1, n2):
    '''Adds two numbers

    Raises error if a non-int is passed as an argument

    :param n1: the first int
    :param n2: the second int'''
    assert_int(n1)
    assert_int(n2)
    return n1 + n2

def assert_int(n):
    '''Raises TypeError if number is not interger'''
    tmp = ("{} is not type int")
    if not isinstance(n, int):
        raise TypeError(tmp.format(n))
    return True

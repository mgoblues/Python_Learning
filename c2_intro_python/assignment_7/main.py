# intergers = range(1, 100)
# print(intergers)

# def return_even(i):
#     even = []
#     for i in intergers:
#         if i % 4 ==0:
#             even.append(i)
#     return even

# print(return_even(intergers))

def filter_custom(l, f):
    '''Filter a list using a function
    return a new list that contains all the elements e of l
        for which f(e) is True

    param l: a list
    param f: a function that takes one argument and retuns either
        True or False'''
    new_list = []
    for e in l:
        if f(e):
            new_list.append(e)
    return new_list

    # return [e for e in l if f(e)]

def map_custom(l, f):
    '''Map a list using a function

    return a new list that applies f(e) for every element e in l

    param l: a list
    param f: a function that takes one argument and retuns a value
    '''
    new_list = []
    for e in l:
        new_list.append(f(e))
    return new_list

def reduce_custom(l, f, starting_value):
    '''Reduce a list using a reducer function and a starting value

    return a single value that applies f(v, e) for every
        e in l from left to right. the initial value for v should be
        starting_value, and subsequent values should be the
        previously valvulated value from f(v,e)

    :param l: a list
    :param f: a function that takes one arg and returns a value
    :param starting_value: the beginning value for the reducer function
        computattion'''

    v = starting_value
    for e in l:
        v = f(v,e)
    return v

# if __name__ == '__main__':
    # '''for map_custom'''
#     l = [7, 8, 9]
#     f = lambda x: x * 10
#     print(map_custom(l, f))

# if __name__ == '__main__':
#     '''for filter_ custom'''
#     l = [7, 8, 9]
#     f = lambda x: x % 4 == 0
#     print(filter_custom(l, f))

if __name__ == '__main__':
    '''for reduce_custom'''
    f = lambda x, y: x + y
    print(reduce_custom([1,2,3,5], f, 0))

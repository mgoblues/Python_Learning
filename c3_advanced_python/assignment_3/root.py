# Trying to have basic data processing over a tuple
from serialize import MySerializer


class MyRootModel(MySerializer):
    '''
    Creating a class that parses desired data form dataset:

    Can run MyRootModel(**dict) and will only take values with an_attr
    and another_attr.

    an_attr should be type <int>
    another_attr should be type <string>
    '''
    my_attrs = {'an_attr': int, 'another_attr': str}

    def __init__(self, **kwargs):
        for k,v in self.my_attrs.items():
            #Iterating over object

            print('These are my keys: {}'.format(k))
            print('These are my values: {}'.format(v))

            #pass the value into v(a function)
            val_type = v(kwargs.get(k))
            # converting kwargs to interger or string

            setattr(self, k, val_type)
            # setting the attribute k as the val_type
            print(k, val_type)


# a = dict(
#     an_attr = 3,
#     another_attr = 'stringgy'
# )

# MyRootModel()



        # for each attr in my_attrs, set
        # self.attr from kwargs
        # can iterate over which
        # kwargs will be dict, ie:
        # { 'an_attr': 'I am an attr',
        # 'another_attr': 6,
        # 'a_third_attr': 'I should not exist'}
        # coercing types: make sure that interger returns interger




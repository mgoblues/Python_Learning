from logging import getLogger, StreamHandler
import logging

# Using Python 2.7 (note print and variable formatting)
# Learning decorators and loggers
# Start by writing simple function
# Then create a decorator (class) that wraps the function
# Use print statements to denote start and end of function
# Once completed [X], try to rewrite and log such that the logging
# will display relevant information in separate file,
# and simple function wont need print function

log = getLogger(__name__)
logging.basicConfig(filename='example.log',level=logging.DEBUG)

class simpleDecorator(object):
    '''Creating a decorator that adds lines before and after function.
    They will be printed in the logger as example.log'''

    def __init__(self, func):
        #Simple constructor
        self.func = func

    def __call__(self, *args, **kwargs):
        #Need the call function to ensure decorator is callable.
        #Logging the function name and arguments to test which function

        log.info('These are my args in %r: %r' % (self.func.func_name, args, ))


        #now execute the original method
        try:
            #run the function, log output, and whether exception is raised
            func_implement = self.func(*args, **kwargs)
            log.info('Output: %r' % (func_implement))
            log.info('No exception raised, exiting the function')
        except Exception, ex:
            #if exception raised, log it, traceback will be linked by default
            log.exception('This is an error')
            raise ex

        return func_implement

@simpleDecorator
def dividingFunction(num, den):
    '''Simple function that divides the second arg from the first'''
    return (num / den)

myDiv = dividingFunction(42.0, 33.22)


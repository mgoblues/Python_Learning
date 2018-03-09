#!/usr/local/bin/python3

#def divideAndConquer(argA, argB): return argA / argB if argB == 0: raise ZeroDivisionError("Woops, divided by zero")

error = False

def divideAndConquer(argA, argB):
    global error
    try:
        return argA / argB;    # try to divide A by B

    except ZeroDivisionError:  # if B is zero, catch this, notify the user and declare an error
        print('  Woops, divided by zero, try again\n')
        error = True

#        raise            # this will print the message and raise the exception causing execution to crash

done = False           


while done is False:   # Loop until we're done, i.e. a <CR> without any input which causes a ValueError exception
    try:
        # get the user input. remove any commas because they might enter "A B" or "A, B"
        a,b=map(int, input("Enter two numbers A, B to calculate A/B (<CR> to exit): ").replace(',',' ').split() )

        # clear any possible errors
        error = False

        # do the division
        x = divideAndConquer(a,b)

        # if we don't have an error, print the result
        if error is False:
            print( '{}/{} = {}'.format( a, b, x ) )

    except ValueError:
        print( "  Thanks, come back again soon\n" )
        done = 1

import logging
logging.basicConfig(level=logging.DEBUG)


def fibonacci(number):
    a = 0
    b = 1
    
    if number == 0:
        return []
    
    if number < 0:
        raise ValueError('number must be > 0')  

    fibonacciSequence = [0]
    # we have one in the list already so number - 1 times
    # this is not the most efficient code
    # could have used yield
    for i in range(1,number):
        fibonacciSequence.append(b)
        # this is funky code make a = b and b = a + b
        a , b = b, a + b
        #logging.debug("%d: %s",number, fibonacciSequence)
    
    return fibonacciSequence


if __name__ == '__main__':
    # tests will go here    
    print("all good")
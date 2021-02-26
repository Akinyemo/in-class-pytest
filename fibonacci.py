# This code is contributed by Saket Modi
# then corrected and improved by Himanshu Kanojiya
# Function for nth Fibonacci number
def fibonacci(n):
    
    if isinstance(n,int) == False:
        raise TypeError('Cannot divide by 0!')

    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        return -1 #modified from printing
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return fibonacci(n-1) + fibonacci(n-2)
 

def test_correct():
    assert fibonacci(5) == 5

def test_incorrect():
    assert fibonacci(1) == 0
 
 

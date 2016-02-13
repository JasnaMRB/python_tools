from math import sqrt

def isPrime(num):
    """
    Determines whether given number is a prime
    Returns boolean
    """
    #check if input is a number :)
    try:
        int(num)
    except:
        return 'Please input a valid number!'
    #turn num to positive
    num = abs(int(num))
    #0, 1 not primes
    if num == 0 or num == 1:
        return False;
    if num == 2:
        return True;
    #other even numbers not prime
    if num % 2 == 0: 
        return False;
    # divide num by all numbers up to and including its square root, starting at 3
    for n in range(3, int(sqrt(num)) + 1):
        if num % n == 0:
            return False;
    return True;

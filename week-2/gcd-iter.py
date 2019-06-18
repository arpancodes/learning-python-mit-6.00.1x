def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    gcd = 1
    smaller = a
    if a > b:
        smaller = b
    for i in range(1, smaller+1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd


print(gcdIter(2, 12))
print(gcdIter(6, 12))
print(gcdIter(3, 12))
print(gcdIter(17, 12))

def gcd(a,b):
    """
    This a modern implementation of Euclide's algorithm using modulus operator
    """
    a =  abs(a)
    b =  abs(b)
    while b > 0:
        a,b = b , a % b
    return a

letter = [chr(i) for i in range(ord('a'),ord('z')+1)] + [chr(i) for i in range(ord('A'),ord('Z')+1)]



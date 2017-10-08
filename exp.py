import math
import sys

parameter = float(sys.argv[1])

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# accurate up to 86th power for positive numbers
def exp(a):
    s = 0;
    for i in range(160):
        s += math.pow(a, i) / factorial(i)
    return s

if __name__ == '__main__':
    a = exp(parameter)
    print str((math.exp(parameter)))  + " is e to the x using math.exp()."
    print str(a) + " calculated using sums."

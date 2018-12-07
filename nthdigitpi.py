"""
nthdigit.py

Get the pi value till the spcified number of digits
reference : https://www.math.hmc.edu/funfacts/ffiles/20010.5.shtml

"""
from __future__ import division
import math
from decimal import Decimal as D
from decimal import getcontext



def calcpi(digit):
    """
    calculate the pi till 'digit' decimal point
    """
    getcontext().prec = digit+1
    pi = D(0)
    for k in range(digit+1):
        pi += D(math.pow(16,-k)) * (D(4/(8*k+1)) - D(2/(8*k+4)) - D(1/(8*k+5)) -D(1/(8*k+6)))
        
    return pi

def main():
    while True:
        try:
            pi_digits = int(input("Enter the number of decimals : "))
        except:
            print("Sorry you did not enter in integers")
            continue
        else:
            break
    
    print(calcpi(pi_digits))
    
if __name__ == "__main__":
    main()
# Name: Georgia Vrana
# Date Submitted: Thursday, March 21st, 2024
# Assignment-7: Compound Interest
# Description: The program defines a getAmount function to calculate and output the amount of
#              compound interest accrued on a principal amount at a given annual interest rate, 
#              compounded monthly, over a specified number of years.

import math

def getAmount(p, r, t):
    """
    Calculate the compound interest.
    
    Parameters:
    p (float): the principal amount (initial investment)
    r (float): the annual interest rate (in percent)
    t (float): the time in years
    
    Returns:
    float: the accumulated amount over the principal after time t
    """
    n = 12
    r_decimal = r / 100  
    amount = p * ((1 + r_decimal / n) ** (n * t))
    return amount

if __name__ == "__main__":
    principal = 1000
    annual_rate = 6
    years = 10    

    final_amount = getAmount(principal, annual_rate, years)

    output = f"${principal} invested at a rate of {annual_rate}% for {years} years is ${final_amount:.2f}"
    print(output)

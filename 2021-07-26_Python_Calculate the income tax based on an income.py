#calculate the income tax based on an income
"Computer Programming Tutor,Jun22,2021"

"""
For the first £5000  there is no Tax, next £15000 there is a 5 %.
Next £4000 there is a 7.5 % surge,and above £50000 is 15%
"""
from bisect import bisect

rates = [0,5,7.5,15] # 5%,7.5%,15%

brackets= [5000,             # first £5000
          20000,            # next £15000
          50000]            # next £25000

btax =[0,             # 5000*0%
         2000,        #25000*10%
           10000]     #50000*20 + 2000

def tax (income):
    i = bisect(brackets,income)
    if not i:
        return 0
    rate = rates[i]
    bracket = brackets[i-1]
    income_in_bracket = income - bracket
    tax_in_bracket = income_in_bracket*rate/100
    totaltax = btax[i-1] + tax_in_bracket
    return totaltax
inc = float(input("Enter the Income ==> £ :"))

print("Total Tax is[£]:",tax(inc))

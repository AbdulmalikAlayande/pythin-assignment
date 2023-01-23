"""
principal = $1000
rate = 7% = 7/100 = 0.07
a = amount after a number of years
n = the number of years
a = p(1 + r)^n
declare variable rate and initialize it to 0.07
declare variable years and initialize it to 10
declare variable principal and initialize it to 1000
declare variable counter and initialize it to 1
while counter is less than or equal to 5
amount equals principal x math.pow((1 + rate), years)
print amount
increment years by 10
"""

import math

rate = 0.07
years = 10
principal = 1000.0
counter = 1
while counter in range(5):
	amount = principal * math.pow((1 + rate),years)
#	print("amount on the $",1000, "principal after", years, "years is: ", amount)
	print("amount on the ${} principal after {} years is: ${}".format(principal, years, amount))
	years += 10
	counter += 1
print()
#Printing Formats
print("amount on the ${0} principal after {1} years is: ${2}".format(principal, years, amount))
print("amount on the ${principal} principal after {years} years is: ${amount}".format(principal = principal, years = years, amount = amount))
print(f"amount on the ${principal} principal after {years} years is: ${amount}")
print("amount on the %.2f principal after %d is: $%.2f"%(principal, years, amount))
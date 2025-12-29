import sys 
from fractions import Fraction
from decimal import Decimal 

ideal_temp = 95.5
current_temp = 95.4999999

print(f"Is the tea at ideal temperature? { ideal_temp }")
print(f"Is the tea not at ideal temperature? { current_temp }")
print(f"Is the tea at ideal temperature (rounded)? { ideal_temp - current_temp }")
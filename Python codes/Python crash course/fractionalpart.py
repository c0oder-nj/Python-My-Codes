import math
def fractional_part(numerator, denominator):
    x = 0
	# Operate with numerator and denominator to 
    # keep just the fractional part of the quotient
    if(denominator == 0):
        x = 0
    elif(numerator == 0):
        x = 0
    elif(numerator == denominator):
        x = 0
    else:
        f,i = math.modf(numerator / denominator)
        x = f
    return x

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
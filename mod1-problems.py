# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."

print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")

# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.

num1 = int(input("Please give me a number:"))
num2 = int(input("Please give me a second number:"))
print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num1 * num2)

# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)

import math
num1 = int(input("Length of side A:"))
num2 = int(input("Length of side B:"))
num3 = int(input("Length of side C:"))
sub = .5 * (num1 + num2 + num3)
print(sub)
area = math.sqrt(sub * (sub - num1) * (sub - num2) * (sub - num2))
print(area)

# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).

import math, statistics
num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))
num3 = int(input("Number 3:"))
num4 = int(input("Number 4:"))
num5 = int(input("Number 5:"))
TOTAL = num1 + num2 + num3 + num4 + num5
print("Total is:", TOTAL)
AVERAGE = TOTAL / 5
print("Average is:", AVERAGE)
RANGE = max(num1, num2, num3, num4, num5) - min(num1, num2, num3, num4, num5)
print("Range is:", RANGE)
MINIMUM = min(num1, num2, num3, num4, num5)
MAXIMUM = max(num1, num2, num3, num4, num5)
print("Minimum is:", MINIMUM)
print("Maximum is:", MAXIMUM)
DATA = (num1, num2, num3, num4,num5)
stdev = statistics.stdev(DATA)
print("The standard deviation is:", stdev)

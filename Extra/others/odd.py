# Code Challenge — Write a program
# Find out if the result of dividing A by B is an odd number.

# The input format:

# The first line is the dividend (A) and the second line is the divider (B). It is guaranteed that the numbers are divided without remainder.

# The output format:

# True or False

# Sample Input 1:

# 99
# 3
# Sample Output 1:

# True

# put your python code here
A = int(input())
B = int(input())

print((A / B) % 2 == 1)

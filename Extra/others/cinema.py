# Code Challenge — Write a program
# The movie theater has N cinema halls that can accommodate K viewers each. Figure out if a movie theater can hold V viewers that plan to visit it on a particular day.

# The input format

# The first line is N cinema halls, the second line is their capacity (K), and the third line is the planned number of viewers (V).

# The output format

# True or False.

# Sample Input 1:

# 9
# 68
# 589
# Sample Output 1:

# True

# put your python code here
N = int(input())
K = int(input())
V = int(input())

print(N * K >= V)

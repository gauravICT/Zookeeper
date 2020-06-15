// When a bank has financial problems the government can return a client's deposit if it is less than 700,000. The interest rate for a particular deposit is 7,1% a year. The percentages are paid to the same deposit at the end of the year and a new value of the interest is calculated.
// Find out how many years it will take for the sum of the deposit to exceed the value protected by the government. 
// The input format:
// The initial sum of the deposit. It is guaranteed that the value will be between 50,000 and 700,000.

// The output format:
// The number of years.

// Sample Input 1:
// 650000

// Sample Output 1:
// 2

// Enter your code here
balance = int(input())
years = 0
while balance < 700000:
    balance = (balance * 1.071)
    years += 1
print(years)

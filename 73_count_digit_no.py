# Write a program to count the digits in a number.
num = int(input("Enter a number: "))
count = 0

while num != 0:
    num //= 10
    count += 1

print("The number of digits in the number is:", count)

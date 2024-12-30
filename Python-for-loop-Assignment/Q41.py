# program to check given number is armstrong or not

number = int(input("Enter a number: "))
num_digits = len(str(number))
sum = 0
for digit in str(number):
    sum += int(digit) ** num_digits
if sum == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
"""Accept input from user
If given number is a multiple of both 3 and 5 prints "Fizz Buzz" instead of number
If given number is a multiple of 3 but not 5 prints "Fizz" instead of number
If given number is a multiple of 5 but not 3 prints "Buzz" instead of number
If given number is not multiple of 3 or 5 prints value as usual."""

userinput=int(input('Enter your number:'))
if userinput%3==0 and userinput%5==0:
    print('FizzBuzz')
elif userinput%5==0:
    print('Buzz')
elif userinput%3==0:
    print('Fizz')
else:
    print(userinput)
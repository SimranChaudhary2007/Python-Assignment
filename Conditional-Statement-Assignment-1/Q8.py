"""Write a Python program that takes an integer input n n. From given number, check if it is divisible by both 3 and 5,
and print "FizzBuzz" if true. If the number is divisible only by 5,print "Buzz." If it is divisible only by 3, print "Fizz." 
Finally, if the number is not divisible by either 3 or 5, print the number itself."""

userinput=int(input('enter your number:'))
if userinput%3==0 and userinput%5==0:
    print('FizzBuzz')
elif userinput%5==0:
    print('Buzz')
elif userinput%3==0:
    print('Fizz')
else:
    print(userinput)
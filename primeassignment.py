# write a program that prompts:
# a user to enter a number checks
# whether a number is prime or odd

# prime numbers
num = 20
if num > 1:
   for i in range(2, (num//2)+1):
       if (num % i) == 0:
        print("the number is not a prime number")
else:
       print("the  number is a prime number")

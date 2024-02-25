#Question 1: FizzBuzz
#Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for 
#multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print 
#"FizzBuzz"


for num in range(1, 101):
  # Check if the number is a multiple of 3 and 5 (divisible by both)
  if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  # Check if the number is a multiple of 3
  elif num % 3 == 0:
    print("Fizz")
  # Check if the number is a multiple of 5
  elif num % 5 == 0:
    print("Buzz")
  # Otherwise, print the number itself
  else:
    print(num)
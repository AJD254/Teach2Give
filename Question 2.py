
#Question 2: Fibonacci Sequence
#Write a program to generate the Fibonacci sequence up to 100.




def fibonacci(n):
  """
  This function generates the Fibonacci sequence up to a given number.

  Args:
      n: The upper limit of the Fibonacci sequence.

  Returns:
      A list containing the Fibonacci sequence up to n.
  """
  # Initialize the first two Fibonacci numbers
  a, b = 0, 1

  # Generate the Fibonacci sequence up to n
  result = []
  for i in range(n):
    result.append(a)
    a, b = b, a + b

  return result

# Generate the Fibonacci sequence up to 100
fibonacci_sequence = fibonacci(100)

# Print the Fibonacci sequence
print(fibonacci_sequence)

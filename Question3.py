#Question 3: Power of Two
#Write a program that takes an integer as input and returns true if the input is a power of two.

def is_power_of_two(n):
    """
    Returns True if n is a power of two.
    """
    if n <= 0:
        # Negative numbers and zero are not powers of two.
        return False
    else:
        # Using bitwise AND to check if n is a power of two.
        # If n is a power of two, (n & (n - 1)) will be 0.
        return n & (n - 1) == 0

# Get input from the user
try:
    num = int(input("Enter an integer: "))
    result = is_power_of_two(num)
    print(f"Is {num} a power of two? {result}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")




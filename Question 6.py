#Question 6: Count Vowels
#Write a program that counts the number of vowels in a sentence.
#eg " Hello World " => returns 2




# Define a function to count the number of vowels in a sentence
def count_vowels(sentence):
    # Define the vowels
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to count the vowels
    num_vowels = sum(1 for char in sentence if char in vowels)
    
    return num_vowels

# Prompt the user to input a sentence
user_input = input("Please enter a sentence: ")

# Call the function with the user's input and print the result
print(count_vowels(user_input))

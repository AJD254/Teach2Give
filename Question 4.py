#Question 4: Capitalize Words
#Write a program that accepts a string as input, capitalizes the first letter of each word in the 
#string, and then returns the result string.
#Examples: 
#"hi"=> returns "Hi"
#"i love programming"=> returns "I Love Programming"



# Define a function to capitalize the first letter of each word in a string
def capitalize_words(input_string):
    # Use the title() method to capitalize the first letter of each word
    result_string = input_string.title()
    return result_string

# Prompt the user to input a string
user_input = input("Please enter a string: ")

# Call the function with the user's input and print the result
print(capitalize_words(user_input))

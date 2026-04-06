# Function to reverse a string
def reversing(s):
    """
    Takes a string as input and returns the reversed string.
    Uses Python slicing for efficiency.
    """
    return s[::-1]

# Taking user input
word = input()
# Calling the function and storing result
result = reversing(word)
# Displaying the result
print(result)



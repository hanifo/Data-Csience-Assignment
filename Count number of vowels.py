# Function to count
def count_vowels(s):
    vowels = "aeiouAEIOU"  # define vowels
    count = 0
    for char in s:  # iterate through each character
        if char in vowels:
            count += 1  # increment if vowel found
    return count

# taking user input
word = input()
# display result
print(count_vowels(word))

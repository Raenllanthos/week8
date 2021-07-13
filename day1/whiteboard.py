# Find Bold Words In String
# Given a string as a parameter to a function, find all of the words inside the string that should be bolded. 
# A bolded word starts with any of the regular vowels in the alphabet. 
# Return the words that should be bolded in a list/array
# Example:
# Input: The Black Dog sits among the apple tree
# Output: [ 'among', 'apple']
# Input: The umbrella company strikes again.
# Output: [ 'umbrella', 'again']

def bold(string):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    words = string.split()
    bolded = []
    for word in words:
        if word[0] in vowels:
            bolded.append(word)
    return bolded

print(bold("The Black Dog sits among the apple tree"))
print(bold("The umbrella company strikes again"))
# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    '''Returns True or False if arguments are anagrams'''
    # [assignment] Add your code here
    splitted_word = sorted(word) # converts the text into a sorted list with each character as an element
    splitted_anagram = sorted(anagram)
    
    # compares the lists returns true or false
    return splitted_word == splitted_anagram
    
    

    

find_anagram('binary','brainy')
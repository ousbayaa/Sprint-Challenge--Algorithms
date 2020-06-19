'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    search = "th" # variable for "th"
    
    if (len(word) == 0 or len(word) < 2): # if no amount of times "th" in a word - return 0
        return 0

    if (word[0:2] == search): # if "th" is at the beginning of the word, return word + 1 (adding to count of how many instances of "th")
        return count_th(word[1:]) + 1
    
    return count_th(word[1:]) # recursion based on the next letter in the word
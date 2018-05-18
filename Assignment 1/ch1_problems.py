from collections import *


#
#   My Solutions to Cracking the Coding interview v.6
#   Luis A. Mireles / Summer 2018
#


# 1.1 is_unique:
#
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
#
# I   : Analyze the string and verify if all chars are unique
# D   : Should return whether true or false if unique or !unique
# E/A : When analyzing string, assign each letter to a set of unique chars
#       when analyzing next chars check if already exists in set, if so return false
# L   : Having dealt with a previous problem (#6 in our first class) analyzing strings
#       with sets was the most beneficial approach i used to solve this problem.
def is_unique(str):
    unique_chars = set()     # create set to store unique chars
    for c in str:
        if c in unique_chars:        # if current char is found in set
            print("not unique string")
            return False
        unique_chars.add(c)
    print("unique string")
    return True


# 1.2 chk_permutation:
#
# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
#
# I   : Take in two strings and analyze if they are permutations
# D   : Should return whether true or false if permutation or !permutation
# E/A : Create a dictionary of size = len(str) that holds an empty char and a 0 value.
#       Then analyzing string 1, assign each letter to dictionary and add +1.
#       When analyzing second string, scan dictionary and -1 from  matching letter.
#       If any cell in dictionary at end has a value not equal to 0, return false
# L   : When building dictionary with char keys, i was able to manipulate the value at each
#       to reflect the number of occurrences, so when checking end array if not = 0  it is not permutation
#       "defaultdict means that if a key is not found in the dictionary, then instead of a KeyError being thrown,
#       a new entry is created. The type of this new entry is given by the argument of defaultdict."

def chk_permutation(string1, string2):
    # check if strings have same length
    if len(string1) is not len(string2):
        print("not permutation")
        return False

    s_count = defaultdict(int)

    # assign c to scan string and add +1
    # for each letter shown
    for c in string1:
        s_count[c] += 1
    print(s_count)

    for c in string2:
        s_count[c] -= 1
    print(s_count)

    if not s_count.values():
        print("is permutation")
        return True
    else:
        print("not permutation")
        return False


# 1.3 urlify:
#
# Write a method to replace all spaces in a string with '%20: You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
#
# Input: "Mr John Smith "J 13
# Output: "Mr%20John%20Smith"
#
# I   : Analyze string and input 20% at every ' ', make sure there's no trailing space at end
# D   : Should return previous string with every space as percent with no trailing space
# E/A : Similar to previous examples we scan string then manipulate each space to hold percent.
#       having done this, we then make sure we don't replace trailing spaces and instead remove it
#       with percents and just omit them from our end goal
# L   : Since strings are immutable in python we convert it to a list and analyze string in reverse.
#       since we have an extra buffer at the end it allows us to change chars without overwriting.

def urlify(in_string, length):
    in_string = list(in_string)
    # enumerate string and scan in reversed order for instances of ' '
    for i, character in reversed(list(enumerate(in_string[0:length]))):
        if character == ' ':
            in_string[i + 3:length + 2] = in_string[i + 1:length]
            in_string[i:i + 3] = '%20'
            length += 2
    return ''.join(in_string)


# 1.4 Palindrome Permutation:
# Given a string, write a function to check if it is a permutation of
# a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
# permutation is a rearrangement of letters. The palindrome does not need to be limited to just
# dictionary words.
#
# Input: Tact Coa
# Output: True (permutations:"taco cat'; "atco cta'; etc.)
#
# I   : Asking for a permutation of a palindrome..
# D   : Return true or false
# E/A : So, palindromes are sets of words that can be mirrored from start to mid and mid to end.
#       This characteristic allows us to check that if a word contains less than 3 letters it is not a
#       palindrome. Since now, it can also be a permutation of any set of letters my strategy is to
#       analyze the letters and count each occurrence. Occurrences for letters should all equal 2 and at
#       most 1 occurrence of another letter that will be the middle letter if odd, else fails.
# L   :

def palindrome_perm(string):
    if len(string) < 3:
        return "not palindrome"
    else:
        for i in str:
            str[i] += 1




def main():
    print("Testing:\n\n")
    # is_unique("dayzz")  # 1.1
    # chk_permutation("strasd", "string")  # 1.2
    # print(urlify("Mr John Smith ", 13))


if __name__ == "__main__":
    main()

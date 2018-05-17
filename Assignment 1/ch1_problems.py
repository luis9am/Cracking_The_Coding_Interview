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


def main():

    is_unique("dayzz")  # 1.1
    chk_permutation("strasd", "string")  # 1.2


if __name__ == "__main__":
    main()

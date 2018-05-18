from collections import defaultdict


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

    # subtract letter count for second
    # letter occurrences
    for c in string2:
        s_count[c] -= 1
    print(s_count)

    # if values are equiv to zero
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
# L   : Since strings are immutable in python we convert it to a list and analyze string in reverse
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
#       This characteristic allows us to confirm if a word contains less than 3 letters it is not a
#       palindrome. Since now, it can also be a permutation of any set of letters my strategy is to
#       analyze the letters and count each occurrence. Occurrences for letters should equal 2 except for the
#       exception of odd length numbers where there can be 1 occurrence of a letter in the middle.
# L   : After having came up with an initial solution of simple incrementing each occurrence of a letter
#       it made it much more difficult to track if an odd length string that has 3+ occurring letters,
#       therefor i changed my implementation to reflect adding and subtracting whenever an occurrence
#       is found, then was able to build cases from either if the string was odd/even length then based
#       on whether the occurrences of the chars in the string met certain criteria would determine this soln

def palindrome_perm(str):
    # remove white-space and assign to dictionary
    string = str.replace(" ", "")
    letter_occurrence_dict = defaultdict(int)

    # count occurrences for each letter in str
    for i in string:

        # if letter exists in string with value
        # greater than zero subtract from total
        if letter_occurrence_dict[i] > 0:
            letter_occurrence_dict[i] -= 1

        # if letter is at zero (for letter occurrences
        # greater the 2) or first time occurrence
        # increment count of occurrence by 1
        else:
            letter_occurrence_dict[i] += 1

    print(letter_occurrence_dict)

    # check if string length is even
    if len(string) % 2 is 0:

        # if length of string is even the dictionary
        # should be filled with values of 0 ( +1 and -1)
        if not letter_occurrence_dict.values():   # doesn't check if values are equal to 2
            print("is even Palindrome / Permutation")
            return True
        else:
            print("not even palindrome")
            return False

    # if length of string is odd
    else:
        # single letter occurrences reflect the number
        # of times a character has only 1 occurrence in str
        single_letters = 0

        # scan to see if there is only one single occurrence
        # of a letter we assume will be the mid of palindrome
        while single_letters < 2:
            if letter_occurrence_dict.values():
                single_letters += 1
            print(single_letters)
            print("is odd palindrome / permutation")
            return True

        # if there are more than two occurences of a single letter
        # we know it is not an odd length palindrome
        print("not palindrome / permutation")
        return False

# 1.5 One Away
# There are three types of edits that can be performen on a string: insert a character, remove a character,
# or replace a character. Given two strings, write a function to check if ther are one edit or zero edits away.
#
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false
#
# I   : Asking if first string is one edit away from second string via an addition of a character or removal
# D   : return true if they are similar enough to be edit away, else false
# E/A : Given a string, I plan to set it to a list and similarly compare it to the second string and marking
#       each time a difference is found. these differences will require analyzing both the strings to determine
#       if it was an insert or removal, an insert would simply adjust the characters after the insertion point +1
#       and a removal to next char after removal -1 position. So if an unexpected character is found when comparing
#       lists we analyze next char in str2 to determine if a new letter was inserted (expected letter will be at next
#       position, or if this is not the case we analyze the second char in first string to determine if a letter was
#       removed.
# L   :
def one_away():
    print("will start soon")


def main():
    print("Testing:\n\n")
    # is_unique("dayzz")    # 1.1
    # chk_permutation("strasd", "string")   # 1.2
    # print(urlify("Mr John Smith ", 13))   # 1.3
    palindrome_perm("tacio a too")    # 1.4 even case doesnt work as intended

if __name__ == "__main__":
    main()

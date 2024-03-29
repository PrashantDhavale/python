# Scenario
# An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.
#
# Your task is to write a program which:
#
# asks the user for two separate texts;
# checks whether, the entered texts are anagrams and prints the result.
# Note:
#
# assume that two empty strings are not anagrams;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check - treat them as non-existent
# Test your code using the data we've provided.
#
# Test data
# Sample input:
#
# Listen
# Silent
#
# Sample output:
#
# Anagrams
#
#
# Sample input:
#
# modern
# norman
#
# Sample output:
#
# Not anagrams

firstWord = input("Enter first word: ").upper()
secondWord = input("Enter second word: ").upper()

if firstWord.strip() == '' or secondWord.strip() == '':
    print("Not anagrams")
foundAll = False
for char in firstWord:
    if char.isspace():
        continue
    if char.isalpha():
        if secondWord.find(char) != -1:
            foundAll = True
            continue
        else:
            foundAll = False
            break

if foundAll:
    print("Anagrams")
else:
    print("Not anagrams")

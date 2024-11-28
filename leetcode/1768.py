"""
1768. Merge Strings Alternately
Easy

You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ''
        if (len(word1) < len(word2)):
            shortest = word1
            longest = word2
        else:
            shortest = word2
            longest = word1
        lenS = len(shortest)
        
        for i in range(len(longest)):
            if (i < lenS):
                output += word1[i] + word2[i]
            else:
                output += longest[i]

        return output

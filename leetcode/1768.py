"""
1768. Merge Strings Alternately

You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Solution Runtime: 25 ms
Beats 97.20%
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ''
        if (len(word1) > len(word2)):
            short = word2
            longest = word1
            
        else:
            short = word1
            longest = word2
        lenS = len(short)
        lenL = len(longest)
        for i in range(lenL):
            if (i < lenS):
                output += word1[i] + word2[i]
            else:
                output += longest[i]
        return output

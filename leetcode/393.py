"""
392. Is Subsequence
Easy

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the 
original string by deleting some (can be none) of the characters 
without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Solution Runtime: 0ms
Beats 100.00%
"""


class Solution(object):
    def isSubsequence(self, s, t):
        j = 0 

        if (s == '') : return True

        for i in range(len(t)):
            if(t[i] == s[j]):
                if (j == len(s) - 1):
                    return True
                j += 1
        return False
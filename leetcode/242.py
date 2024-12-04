"""
242. Valid Anagram
Easy

Given two strings s and t, return true if t is 
an anagram of s, and false otherwise.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = defaultdict(int)
        t_count = defaultdict(int)

        if (len(s) != len(t)):
            return False

        for i in range(len(s)):
            s_count[s[i]] += 1
            t_count[t[i]] += 1

        if (s_count == t_count):
            return True
        return False
            
            
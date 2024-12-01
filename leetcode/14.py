"""
14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ''
        broken = False
        
        shortest = len(strs[0])
        for word in strs:
            if len(word) < shortest:
                shortest = len(word)

        for i in range (shortest):
            check = strs[0][i]
            for word in strs:
                if (word[i] != check):
                    broken = True
                    break
            if (not broken):
                output += word[i]
            else:
                break

        return output

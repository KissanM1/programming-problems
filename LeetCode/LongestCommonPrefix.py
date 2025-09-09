"""
===============================
14. Longest Common Prefix
===============================

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        minLen = len(strs[0])
        for word in strs:
            minLen = min (minLen, len(word))

        for j in range(minLen):
            broken = False
            for i in range(len(strs) - 1):
                print(strs[i][j], strs[i])
                if strs[i][j] != strs[i + 1][j]:
                    print ("broke at", strs[i][j], strs[i])
                    broken = True
            if not broken:
                prefix.append(strs[0][j])
            else:
                break
        return "".join(prefix)

        
            
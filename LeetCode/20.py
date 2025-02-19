"""
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string 
is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        openings = ['(', '{', '[']
        closings = {')':'(','}':'{',']':'['}
        for letter in s:
            if letter in openings:
                stack.append(letter)
            if letter in closings:
                if (not stack):
                    return False
                if stack.pop() != closings[letter]:
                    return False
        if (len(stack) > 0):
            return False
        return True
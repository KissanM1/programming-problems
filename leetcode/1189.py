"""
1189. Maximum Number of Ballons
Easy

Given a string text, you want to use the characters of 
text to form as many instances of the word "balloon" as 
possible.

You can use each character in text at most once. Return 
the maximum number of instances that can be formed.
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = defaultdict(int)
        minimum = float('inf')
        count = 0
        for letter in text:
            letters[letter] += 1

        letters['l'] //= 2
        letters['o'] //= 2

        for key, value in letters.items():
            if key in 'ballon':
                count += 1
                if value < minimum:
                    minimum = value
        if (count < len(set('ballon'))):
            return 0
            
        return minimum
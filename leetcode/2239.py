"""
2239. Find Closest Number to Zero
Easy 

Given an integer array nums of size n, return the number with the value closest to 0 in nums. 
If there are multiple answers, return the number with the largest value.
"""

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        lowest = 10**100
        for num in nums:
            if (abs(0 - num) < abs(lowest)):
                lowest = num
            if (abs(0 - num) == abs(lowest)):
                if (num > lowest):
                    lowest = num
        return lowest
        
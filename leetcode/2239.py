"""
2239. Find Closest Number to Zero
Easy

Given an integer array nums of size n, return the number with the value closest to 0 in nums. 
If there are multiple answers, return the number with the largest value.

Solution Runtime: 7ms
Beats 43.93%
"""

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        lowestDifference = -9999999999999
        for num in nums:
            diff = abs(0 - num)
            if (diff < abs(lowestDifference)):
                lowestDifference = num
            elif (num > lowestDifference and diff == abs(lowestDifference)):
                lowestDifference = num
        return lowestDifference

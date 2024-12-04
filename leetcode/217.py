"""
217. Contains Duplicates
Easy

Given an integer array nums, return true if any value 
appears at least twice in the array, and return false 
if every element is distinct.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: 

        output = len(list(set(nums))) == len(nums)
        return not output
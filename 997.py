"""
997. Squares of a Sorted Array
Easy

Given an integer array nums sorted in non-decreasing 
order, return an array of the squares of each number 
sorted in non-decreasing order.
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        output = []

        for i in range(len(nums)):
            nums[i] *= nums[i]

        while left <= right:
            if nums[left] > nums[right]:
                output.append(nums[left])
                left += 1
            else:
                output.append(nums[right])
                right -= 1
        output.reverse()
        return output
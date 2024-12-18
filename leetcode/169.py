"""
169. Majority Element
Easy

Given an array nums of size n, return the majority element.
The majority element is the element that appears more 
than ⌊n / 2⌋ times. You may assume 
that the majority element always exists in the array.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        for key, value in counter.items():
            if value > len(nums) / 2 :
                return key

        print(counter)
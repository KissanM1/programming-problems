"""
228. Summary Ranges
Easy

A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers 
in the array exactly. That is, each element of nums is covered by 
exactly one of the ranges, and there is no integer x such that x is 
in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums.append('')
        output = []
        start = nums[0]
        for i in range(1, len(nums)):
            if (nums[i] != nums[i - 1] + 1):
                end = nums[i - 1]
                if (start == end):
                    output.append(f"{start}")
                else:
                    output.append(f"{start}->{end}")
                start = nums[i]
        return output



        
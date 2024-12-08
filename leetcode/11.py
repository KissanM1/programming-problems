"""
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two 
endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a 
container, such that the container contains the most 
water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:

            length = right - left
            if (height[left] < height[right]):
                area = height[left] * length
                left += 1
            else:
                area = height[right] * length
                right -= 1

            if area > maxArea:
                maxArea= area

        return maxArea
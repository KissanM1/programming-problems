"""
56. Merge Intervals
Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all 
overlapping intervals, and return an array of the non-overlapping intervals 
that cover all the intervals in the input.
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort(key=lambda L: L[0])        
        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            current_start = intervals[i][0]
            current_end = intervals[i][1]
            if (current_end <= end):
                continue
            if (current_start <= end):
                print(current_start, end)
                end = current_end
            else:
                output.append([start, end])
                start = current_start
                end = current_end
        
            print(start, end, current_start, current_end)
        output.append([start, end])
        return output
"""
682. Baseball Game
Easy

You are keeping the scores for a baseball game with strange rules. At the beginning of the game, 
you start with an empty record.
You are given a list of strings operations, where operations[i] is the ith operation you must apply 
to the record and is one of the following:
An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.
The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit 
integer and that all operations are valid.
"""

class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        for op in operations:
            if(op == '+'):
                right = stack.pop()
                left = stack.pop()
                stack.append(left)
                stack.append(right)
                stack.append(left + right)
            elif (op == 'D'):
                temp = stack[-1]
                stack.append(temp * 2)
            elif (op == 'C'):
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)
        

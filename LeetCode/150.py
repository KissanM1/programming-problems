"""
150. Evaluate Reverse Polish Notation
Medium

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.
Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ops = ['+','-','*','/']
        stack = []
        for token in tokens:
            if token in ops:
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                else:
                    stack.append(int(float(left) / float(right)))  # Division is weird, had to type cast to floats so 6 // -132 did not return -1
            else:
                stack.append(int(token))
        return stack[0]
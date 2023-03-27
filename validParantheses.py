# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'(': ')', '[': ']', '{': '}'}

        for char in s:
            if char in d:
                stack.append(char)
            elif not stack or d[stack.pop()] != char:
                return False
                
        return not stack
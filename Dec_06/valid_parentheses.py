# Day 06 of Christmas Coding Challenge
# Problem statement:
# https://leetcode.com/problems/valid-parentheses/

# This solution uses a stack which is an LIFO data structure.

class Solution:
    from collections import deque

    def isValid(self, s: str) -> bool:
        
        stack = deque()
        lefts =  ['(', '{', '[']
        rights = [')', '}', ']']

        map_r2l = dict(zip(rights, lefts))

        for c in s:
            if c in lefts:
                stack.append(c)
            else:
                if len(stack)==0:
                    return False
                else:
                    if stack.pop() != map_r2l[c]:
                         return False

        if len(stack)==0:
            return True

        return False


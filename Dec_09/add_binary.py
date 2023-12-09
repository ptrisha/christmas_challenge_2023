# Day 9 of Christmas Challenge
# Problem statement:
# https://leetcode.com/problems/add-binary

class Solution:

    def addBinary(self, a: str, b: str) -> str:

        int_a = int(a, 2)
        int_b = int(b, 2)      
        sum_str = bin(int_a + int_b)[2:]

        return sum_str


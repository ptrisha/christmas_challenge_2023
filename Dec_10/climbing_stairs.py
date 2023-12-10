# Day 10 of Christmas Challenge with Leetcode problem
# Problem description:
# https://leetcode.com/problems/climbing-stairs/

import math

class Solution:
    def climbStairs(self, n: int) -> int:
        
        sum_ways = 0
        max_num_2_steps = n//2
        for i in range(1, max_num_2_steps+1):
            # calculate total number of steps given i number of 2-steps
            total_steps = n - i      # comes from: n - 2*i + i
            sum_ways += math.comb(total_steps, i)
        
        return (sum_ways+1)

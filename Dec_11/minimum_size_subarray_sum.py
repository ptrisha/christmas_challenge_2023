# Day 11 Leetcode problen
# Problem description:
# https://leetcode.com/problems/minimum-size-subarray-sum/

# This version exceeds the time limit.
# Will use the sliding window algorithm in the next version.

class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if max(nums) >= target:
            return 1
        # From here, we deal with cases where the numbers are < target
        # iterate through length of subsequence
        # inner loop through moving window of subsequence length
        for i in range(1, len(nums)+1):
            for j in range( len(nums) - i + 1):
                if sum( nums[j:j+i] ) >= target:
                    return i
        
        return 0

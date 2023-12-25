# Day 11 Leetcode problen
# Problem description:
# https://leetcode.com/problems/minimum-size-subarray-sum/

# This version uses the sliding window algorithm.  It passes all the
# submission test cases on Leetcode, and does not exceed the time limit.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    
        head = tail = currSum = 0
        length = len(nums)
        minLength = length+1


        while head < length:
            currSum += nums[head]

            if currSum >= target:
                # try to move up the tail
                minLength = min(minLength, head-tail+1)

                while (currSum-nums[tail] >= target) and (tail < head):
                       currSum -= nums[tail]
                       if (head-tail) < minLength:
                           minLength = head-tail
                       tail += 1
            head += 1
            
            
        if minLength > length:
            minLength = 0
        
        return minLength



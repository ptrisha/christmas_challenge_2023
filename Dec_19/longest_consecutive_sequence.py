# Leetcode problem for Dec 19
# Problem description:
# https://leetcode.com/problems/longest-consecutive-sequence

# This is my second version, implemented with the help of a hint from the
# Leetcode discussion forum.  The submission did not exceed memory or time
# limits, but in comparison with other Python solutions submitted on Leetcode,
# this version is relative slow and inefficient in terms of memory.

class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums)==1:
            return 1

        min_num = min(nums)
        #max_num = max(nums)

        nums_set = set(nums)
        max_len = -1
        
        for num in nums:
            # determine if num is the possible start of a subsequence
            if (num==min_num) or ((num-1) not in nums_set):
                # find the length of the subsequence
                curr_len = 1
                while ((num+curr_len) in nums_set):
                    curr_len += 1
                # update max_len
                if curr_len > max_len:
                    max_len = curr_len

        return max_len
    
    
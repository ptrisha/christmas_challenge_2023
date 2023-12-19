# Leetcode problem for Dec 19
# Problem description:
# https://leetcode.com/problems/longest-consecutive-sequence

# This version exceeds the time limit set by Leetcode for at least
# one of the test cases.  A faster version will be committed soon.

class Solution:

    #import bitarray

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums)==1:
            return 1

        min_num = min(nums)
        max_num = max(nums)

        # declare a True/False array for consecutive numbers ranging from
        # min_num to max_num
        #bits = [False]*(max_num-min_num+1)
        #bits = bitarray(max_num-min_num+1)
        #bits.setall(0)
        bits = 0 << (max_num-min_num+1)

        # for each number, mark its bit True in bits
        for num in nums:
            indx = num - min_num
            #bits[indx] = True
            bits = ( bits | 1<<(indx+1) )

        #print(bits)

        # loop thru bits and compute lengths of subsequences
        max_len = 0
        curr_len = 0
        mask = 1
        for i in range(max_num-min_num+1):
            mask = mask << 1
            #if bits[i]:   # current bit is True
            if bits & mask:
               curr_len += 1
            else:              
               max_len = max(curr_len, max_len)
               curr_len = 0

        max_len = max(curr_len, max_len)

        return max_len
    
    
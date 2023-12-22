# Leetcode problem for Dec 22, just 2 more days to Christmas Day
# Problem description:
# https://leetcode.com/problems/single-number-ii

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        unique_nums = list(set(nums))
        unique_sum = sum(unique_nums)

        for num in unique_nums:
            hyp_total = num + 3*(unique_sum - num)
            if hyp_total == total:
                return num
            

# Day 08 of Christmas Challenge with Leetcode problems
# Problem statement:
# https://leetcode.com/problems/search-insert-position/

# My solution uses binary search which is O(log n).

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high)//2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                return mid

        if target > nums[mid]:
            return mid+1
        else:
            if mid > 0:
                return mid
            else:
                return 0

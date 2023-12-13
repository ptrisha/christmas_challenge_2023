# Day 13 of Leetcode problems
# Problem description:
# https://leetcode.com/problems/search-a-2d-matrix

# This version uses binary search on the first column to identify
# the possible row that may contain the target.  Then a binary search
# is executed on that row.  The complexity is thus O( log m + log n)= O(log mxn).

class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        def binSearchList(nums: List[int], target: int) -> (bool, int):
            low = 0
            high = len(nums) - 1
            while low <= high:
                mid = (low + high)//2
                if target > nums[mid]:
                    low = mid + 1
                elif target < nums[mid]:
                    high = mid - 1
                else:
                    return (True, mid)

            # in this case, low > high
            return (False, low-1)
        
        first_col = [ matrix[i][0] for i in range(len(matrix))]
        
        found, row = binSearchList(first_col, target)

        if found:
            return True
        
        return binSearchList(matrix[row], target)[0]

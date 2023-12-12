# Day 12 of Leetcode problems
# Problem description:
# https://leetcode.com/problems/triangle/

# This is a preliminary version of the solution.
# It does not work for all of the test cases.
# Will try dynamic programming version for next version.

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        min_path = triangle[0][0]
        ind = 0
        for row in triangle[1:]:
            if row[ind] > row[ind+1]:
                min_path += row[ind+1]
                ind += 1
            else:
                min_path += row[ind]
        return min_path



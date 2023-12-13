# Day 12 of Leetcode problems
# Problem description:
# https://leetcode.com/problems/triangle/

# This is the second version of my solution.
# This version passes all test cases.


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        if len(triangle)==1:
            return triangle[0][0]

        # get the path sums for the second row
        triangle[1][0] += triangle[0][0]
        triangle[1][1] += triangle[0][0]

        for i in range(2, len(triangle)):  # iterate through rows
            for j in range(len(triangle[i])):  # iterate thru cols in the row
                if j==0:
                    triangle[i][j] += triangle[i-1][0]
                elif j==len(triangle[i])-1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j] )

        min_path = min( triangle[-1] )

        return min_path
    


# Day 7 of Christmas Challenge
# Problem statement:
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# I adapted the algorithm taught on Youtube channel linked below:
# https://www.youtube.com/watch?v=bqraplP_Kqk

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def construct(start, end):
            if start > end:
               return None
            mid = start + (end - start)//2
            left_child = construct(start, mid-1)
            tnode = TreeNode(val=nums[mid], left=left_child)
            tnode.right = construct(mid+1, end)
            return tnode

        root = construct(0, len(nums)-1)

        return root


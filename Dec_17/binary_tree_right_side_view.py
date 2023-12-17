# Leetcode problem Day 17
# Problem description:
# https://leetcode.com/problems/binary-tree-right-side-view

# The basic idea is to find the rightmost node at each level of the tree,
# regardless of whether the node is a left or right child of some parent node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        rightSideNodes = []
        parents = []
        if root:
           parents.append(root)

        #while any([True for parent in parents if parent is not None]):
        while parents:
            rightmostNode = parents[-1]
            rightSideNodes.append(rightmostNode.val)

            children = []

            # get the non-null children of each parent
            for parent in parents:
                if parent.left:
                    children.append(parent.left)
                if parent.right:
                    children.append(parent.right)

            parents = []
            parents.extend(children)

        return rightSideNodes

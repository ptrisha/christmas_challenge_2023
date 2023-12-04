# Link to problem statement:
# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Note: This is the second version of my solution.  It works for
#       all test cases that were run on Leetcode.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # traverse tree breadth-first fashion and store nodes of each level in a list
        que= [root]
        vals = []
        # check that the node list is not all nulls
        while any([True for x in que if x is not None]):
             subvals = []
             new_nodes = []
             for nd in que:
                 if nd is not None:
                     subvals.append(nd.val)
                     new_nodes.append(nd.left)
                     new_nodes.append(nd.right)

             vals.append(subvals)
             que = new_nodes

        avgs = [ sum(ll)/len(ll) for ll in vals]
        return avgs
    
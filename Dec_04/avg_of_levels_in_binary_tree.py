# Link to problem statement:
# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Note: The solution below does not work for all the testcases.
# I will continue working on it.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # traverse tree breadth-first fashion and store node values in a list
        level = 0
        avgs = []
        que = [root]
        within_lvl_count = 0
        within_lvl_sum = 0
        within_lvl_non_null = 0
        while any([True for x in que if x is not None]):
            node = que.pop(0)
            within_lvl_count += 1

            if node is not None:
               que.append(node.left)
               que.append(node.right)
            if node is not None:
               within_lvl_sum += node.val
               within_lvl_non_null += 1

            if within_lvl_count == 2**level:              
                avg = within_lvl_sum/within_lvl_non_null
                avgs.append(avg)
                # reset within_level_counter and level tracker
                level += 1
                within_lvl_sum = 0
                within_lvl_count = 0
                within_lvl_non_null = 0
        
        if (within_lvl_count < 2**level) and (within_lvl_non_null > 0):
            avg = within_lvl_sum/within_lvl_non_null
            avgs.append(avg)

        return avgs

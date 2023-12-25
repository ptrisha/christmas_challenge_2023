# Leetcode problem for Dec 25 (!)
# Problem description:
# https://leetcode.com/problems/binary-tree-maximum-path-sum

# This solution uses DFS.  It was challenging for me, but
# thanks to the Lord of Christmas, the solution came together.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import sys

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = -1000000
        visited = set()

        if (root.left is None) and (root.right is None):
            return root.val
        
        def isLeaf(currNode: TreeNode) -> bool:
            if (currNode.left is None) and (currNode.right is None):
                return True
            return False

        def dfs(currNode: TreeNode, maxPath: int) -> [int, int]: 
            
            if currNode not in visited:
                visited.add(currNode)               
                
                if isLeaf(currNode):
                    if currNode.val > maxPath:
                        maxPath = currNode.val
                    return [currNode.val, maxPath]
                 
                adjLeft = adjRight = -1000000
                if currNode.left:
                    adjLeft, maxPath = dfs(currNode.left, maxPath)
                if currNode.right:
                    adjRight, maxPath = dfs(currNode.right, maxPath)

                currVal = currNode.val
                maxAdjPath = max(adjLeft+currVal, adjRight+currVal, currVal)
                #print(f"CurrVal: {currVal} adjLeft: {adjLeft} adjRight: {adjRight}")
                
                if maxAdjPath > maxPath:
                    maxPath = maxAdjPath
                if (adjLeft+currVal+adjRight) > maxPath:
                    maxPath = adjLeft+currVal+adjRight
                return [maxAdjPath, maxPath]

            return [0, maxPath]



        sumPath, maxPath = dfs(root, maxPath)

        return maxPath        

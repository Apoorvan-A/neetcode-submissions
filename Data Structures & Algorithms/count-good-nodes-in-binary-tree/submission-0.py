# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,max1):
            if not node:    
                return 0
            if node.val>=max1:
                newMax=node.val
                good=1
            else:
                newMax=max1
                good=0
            good+=dfs(node.left,newMax)
            good+=dfs(node.right,newMax)
            return good
        return dfs(root,float('-inf'))
    

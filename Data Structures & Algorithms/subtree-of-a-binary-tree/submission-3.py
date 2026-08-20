# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def issame(node1,node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val!=node2.val:
                return False
            left=issame(node1.left,node2.left)
            right=issame(node1.right,node2.right)
            return left and right
        res=False
        def dfs(root,subroot):
            nonlocal res
            if not root:
                return 
            if root.val==subroot.val:
                res=res or issame(root,subroot)
            dfs(root.left,subroot)
            dfs(root.right,subroot)
        dfs(root,subRoot)
        return res

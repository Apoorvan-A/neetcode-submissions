# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=1
        self.res=0
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            nonlocal count
            if count==k:
                self.res=node.val
            count+=1
            inorder(node.right)
        inorder(root)
        return self.res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res=[]
        flag=True
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            if res:
                if root.val>res[-1]:
                    res.append(root.val)
                else:
                    nonlocal flag
                    flag=False
            else:
                res.append(root.val)
            inorder(root.right)
        inorder(root)
        return flag
        '''for i in range(len(res)-1):
            if res[i]<res[i+1]:
                continue
            else:
                return False
        return True'''
            
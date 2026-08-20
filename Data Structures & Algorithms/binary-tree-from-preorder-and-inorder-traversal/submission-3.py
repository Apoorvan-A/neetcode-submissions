# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preidx=0
        inmap={}
        for i,n in enumerate(inorder):
            inmap[n]=i
        def dfs(left,right):
            nonlocal preidx
            if left>right:
                return
            node=TreeNode(preorder[preidx])
            preidx+=1
            mid=inmap[node.val]
            node.left=dfs(left,mid-1)
            node.right=dfs(mid+1,right)
            return node

        return dfs(0,len(inorder)-1)
        
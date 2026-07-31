"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        OldToNew={}

        def dfs(node):
            if node in OldToNew:
                return  
            copy=Node(node.val)
            OldToNew[node]=copy

            for nei in node.neighbors:
                dfs(nei)
        dfs(node)

        for c in OldToNew:
            for nei in c.neighbors:
                OldToNew[c].neighbors.append(OldToNew[nei])

        return OldToNew[node]
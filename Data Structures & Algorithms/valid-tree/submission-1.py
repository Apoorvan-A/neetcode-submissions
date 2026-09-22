class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        
        adj=defaultdict(list)
        visited=set()
        for node1,node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
        dfs(0)
        return len(visited)==n
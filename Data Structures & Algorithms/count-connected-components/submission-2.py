class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n==0:
            return 0
        adj=defaultdict(list)
        visited=set()
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)


        def dfs(node):
            if node in visited:
                return 
            visited.add(node)

            for nei in adj[node]:
                dfs(nei)
        res=1
        dfs(0)
        for node in range(n):
            if node not in visited:
                res+=1
                dfs(node)
        return res
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()
        for source, dest in tickets:
            adj[source].append(dest)

        route = []

        def dfs(src):
            while adj[src]:
                nxt = adj[src].pop(0)
                dfs(nxt)
            route.append(src)

        dfs("JFK")
        return route[::-1]
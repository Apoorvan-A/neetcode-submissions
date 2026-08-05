class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=defaultdict(list)
        for u,v,t in times:
            adj[u].append([v,t])
        def dijkstra(source,adj):
            dist=[float('inf')]*(n+1)
            dist[source]=0

            heap=[[0,source]]
            while heap:
                t1,n1=heapq.heappop(heap)
                if t1>dist[n1]:
                    continue
                for n2,t2 in adj[n1]:
                    new_time=t1+t2

                    if new_time<dist[n2]:
                        dist[n2]=new_time
                        heapq.heappush(heap,[new_time,n2])
            return dist
        res=dijkstra(k,adj)
        return max(res[1:]) if max(res[1:])!=float('inf') else -1
        


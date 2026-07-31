class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])
        pacific=set()
        atlantic=set()
        res=[]
        def dfs(r,c,visited,prev):
            if (r<0 or c<0 or r>=rows or c>=cols or heights[r][c]<prev or (r,c) in visited):
                return
            prev=heights[r][c]
            visited.add((r,c))
            dfs(r+1,c,visited,prev)
            dfs(r-1,c,visited,prev)
            dfs(r,c+1,visited,prev)
            dfs(r,c-1,visited,prev)
        
        for c in range(cols):
            dfs(0,c,pacific,heights[0][c])
            dfs(rows-1,c,atlantic,heights[rows-1][c])

        for r in range(rows):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,cols-1,atlantic,heights[r][cols-1])

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res
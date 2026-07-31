class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res=0
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        directions=[[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(r,c):
            queue=deque()
            visited.add((r,c))
            queue.append((r,c))
            area =1

            while queue:
                row,col=queue.popleft()
                for dr,dc in directions:
                    nr,nc=row+dr,col+dc
                    if(0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1 and (nr,nc) not in visited):
                        visited.add((nr,nc))
                        queue.append((nr,nc))
                        area+=1
            return area    
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in  visited:
                    res=max(res,bfs(r,c))
        return res

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        queue=deque()
        def visit(r,c):
            if (r,c) in visited or r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==-1:
                return
            visited.add((r,c))
            queue.append([r,c])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    queue.append([r,c])
                    visited.add((r,c))
        dist=0
        while queue:
            for i in range(len(queue)):
                r,c=queue.popleft()
                grid[r][c]=dist
                visit(r,c+1)
                visit(r,c-1)
                visit(r+1,c)
                visit(r-1,c)
            dist+=1
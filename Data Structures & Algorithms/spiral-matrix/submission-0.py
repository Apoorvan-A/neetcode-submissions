class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix:
            return []

        rows=len(matrix)
        cols=len(matrix[0])
        visited=set()
        res=[]

        dirn=[(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(r,c,direction):
            visited.add((r,c))
            res.append(matrix[r][c])

            nr=r+dirn[direction][0]
            nc=c+dirn[direction][1]

            if nr<0 or nr>=rows or nc<0 or nc>=cols or (nr,nc) in visited:
                direction=(direction+1)%4
                nr=r+dirn[direction][0]
                nc=c+dirn[direction][1]
            
            if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited:
                dfs(nr,nc,direction)
            
        dfs(0,0,0)
        return res
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows=len(board)
        cols=len(board[0])
        visited=set()
        def dfs(r,c,visited):
            if (r<0 or c<0 or r>=rows or c>=cols or board[r][c]!="O" or (r,c) in visited):
                return 
            visited.add((r,c))
            board[r][c]="T"
            dfs(r+1,c,visited)
            dfs(r-1,c,visited)
            dfs(r,c+1,visited)
            dfs(r,c-1,visited)
        for r in range(rows):
            if board[r][0]=="O":
                dfs(r,0,visited)
            if board[r][cols-1]=="O":
                dfs(r,cols-1,visited)
        
        for c in range(cols):
            if board[0][c]=="O":
                dfs(0,c,visited)
            if board[rows-1][c]=="O":
                dfs(rows-1,c,visited) 

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                if board[r][c]=="T":
                    board[r][c]="O"
    

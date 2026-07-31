class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        s=word
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        rows=len(board)
        cols=len(board[0])
        visited=set()

        def dfs(i,row,col):
            if i==len(s):
                return True
            if i>=len(s) or row<0 or col<0 or row>=rows or col>=cols or board[row][col]!=s[i] or (row,col) in visited:
                return False
            
            visited.add((row,col))
            found=dfs(i+1,row-1,col) or dfs(i+1,row+1,col) or dfs(i+1,row,col+1) or dfs(i+1,row,col-1)
            visited.remove((row,col))
            return found
        res=False
        for r in range(rows):
            for c in range(cols):
                if s[0]==board[r][c]:
                    res=res or dfs(0,r,c)
        return res

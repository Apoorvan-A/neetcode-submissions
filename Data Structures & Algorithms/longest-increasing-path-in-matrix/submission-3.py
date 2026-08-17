class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row=len(matrix)
        col=len(matrix[0])
        memo={}
        def dfs(r,c,prev):
            if r<0 or c<0 or r>=row or c>=col  or matrix[r][c]<=prev :
                return 0
            if((r,c) in memo):
                return memo[(r,c)]
            prev=matrix[r][c]
            res= 1+max(dfs(r-1,c,prev),dfs(r,c-1,prev),dfs(r+1,c,prev),dfs(r,c+1,prev))
            memo[(r,c)]=res
            return res
        res=-float('inf')
        for r in range(row):
            for c in range(col):
                res=max(res,dfs(r,c,-1))
        return res
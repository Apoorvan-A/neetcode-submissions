class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp={}
        def dfs(i,string):
            if string==t:
                return 1
            if i==len(s):
                return 0
            if (i,string) in dp:
                return dp[(i,string)]
            res=dfs(i+1,string+s[i])+dfs(i+1,string)
            dp[(i,string)]=res
            return res
        return dfs(0,"")
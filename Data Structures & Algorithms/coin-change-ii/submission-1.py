class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp={}
        def dfs(i,target):
            if target==0:
                return 1
            if target<0 or i==len(coins):
                return 0
            if (i,target) in dp:
                return dp[i,target]
            res=dfs(i,target-coins[i])+dfs(i+1,target)
            dp[(i,target)]=res
            return res
        return dfs(0,amount)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def dfs(i,amount):

            if  i==len(nums):
                if amount==target:
                    return 1
                else:
                    return 0
            if (i,amount) in dp:
                return dp[(i,amount)]
            res=dfs(i+1,amount-nums[i])+dfs(i+1,amount+nums[i])
            dp[(i,amount)]=res
            return res
        return dfs(0,0)
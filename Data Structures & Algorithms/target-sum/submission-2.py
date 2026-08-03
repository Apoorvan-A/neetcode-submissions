class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
    
        def dfs(i,amount):

            if  i==len(nums):
                if amount==target:
                    return 1
                else:
                    return 0
            
            res=dfs(i+1,amount-nums[i])+dfs(i+1,amount+nums[i])
            return res
        return dfs(0,0)
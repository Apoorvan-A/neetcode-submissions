class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        target=sum(nums)//2
        memo={}
        def dfs(i,curr):
            if curr==0:
                return True 
            if curr<0 or i == len(nums):
                return False
            if (i,curr) in memo:
                return memo[(i,curr)]
            res=dfs(i+1,curr-nums[i]) or dfs(i+1,curr)
            memo[(i,curr)]=res
            return res
        
        return dfs(0,target)
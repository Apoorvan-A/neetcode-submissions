class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        def dfs(i,sub,target):
            if target==0:
                res.append(sub.copy())
                return
            

            for j in range(i,len(nums)):
                if nums[j]>0 and nums[j]==nums[j-1]:
                    return
                if target-nums[j]<0:
                    return
                sub.append(nums[j])
                dfs(j,sub,target-nums[j])
                sub.pop()
        dfs(0,[],target)
        return res
                
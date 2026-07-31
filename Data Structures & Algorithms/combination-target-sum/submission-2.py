class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        def backtrack(idx,subset,current_sum):
            if current_sum==target:
                res.append(subset.copy())
                return
            if idx == len(nums):
                return  
            for i in range(idx,len(nums)):
                if current_sum+nums[i]>target:
                    return  
                subset.append(nums[i])
                backtrack(i,subset,current_sum+nums[i])
                subset.pop()
        backtrack(0,[],0)
        return res
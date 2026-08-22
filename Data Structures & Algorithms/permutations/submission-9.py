class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm=[]
        res=[]
        picked=[False]*len(nums)
        def dfs():
            if len(perm)==len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if not picked[i]:
                    perm.append(nums[i])
                    picked[i]=True
                    dfs()
                    perm.pop()
                    picked[i]=False
        dfs()
        return res


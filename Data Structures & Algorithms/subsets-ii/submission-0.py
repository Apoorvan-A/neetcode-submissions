class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sub=[]
        final=[]
        def dfs(i):
            if i==len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            dfs(i+1)
            sub.pop()
            dfs(i+1)
        dfs(0)
        for l in res:
            l.sort()
            if l not in final:
                final.append(l)
        return final
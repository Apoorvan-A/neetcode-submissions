class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        def backtrack(idx,subset):
            if idx == n:
                res.append(subset.copy())
                return
            subset.append(nums[idx])
            backtrack(idx+1,subset)
            subset.pop()
            backtrack(idx+1,subset)
        backtrack(0,[])
        return res
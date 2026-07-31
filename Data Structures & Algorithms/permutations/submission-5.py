class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        visited=set()
        def backtrack(visited,subset):
            if len(subset)==len(nums):
                res.append(subset.copy())
                return

            for num in nums:
                if num not in visited:   
                    subset.append(num)
                    visited.add(num)
                    backtrack(visited,subset)
                    subset.pop()
                    visited.remove(num)
        backtrack(visited,[])
        return res
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result=max_so_far=min_so_far=nums[0]

        for i in range(1,len(nums)):
            curr=nums[i]
            candidates=(curr,max_so_far*curr,min_so_far*curr)
            max_so_far=max(candidates)
            min_so_far=min(candidates)
            result=max(result,max_so_far)
        return result
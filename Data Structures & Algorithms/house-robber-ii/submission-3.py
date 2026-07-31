class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))

    def helper(self,nums):
        rob1,rob2=0,0
        
        for num in nums:
            rob1,rob2=max(num+rob2,rob1),rob1
        
        return rob1
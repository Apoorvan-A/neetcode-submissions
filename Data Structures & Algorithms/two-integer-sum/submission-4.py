class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            new_target = target-nums[i]
            if new_target in nums[i+1:]:
                    return [i,nums.index(new_target,i+1)]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break  # smallest remaining num is positive, no triplet can sum to 0
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate starting points

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1  # skip duplicate left values
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1  # skip duplicate right values

        return res
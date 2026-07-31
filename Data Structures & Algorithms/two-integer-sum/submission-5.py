class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index

        for i, num in enumerate(nums):
            complement = target - num

            # If we have already seen the complement,
            # we found the two numbers.
            if complement in seen:
                return [seen[complement], i]

            # Store the current number and its index.
            seen[num] = i
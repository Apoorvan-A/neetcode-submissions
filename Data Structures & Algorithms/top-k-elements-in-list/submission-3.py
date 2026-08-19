class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        arr = [[] for _ in range(len(nums) + 1)]

        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        for key in count:
            arr[count[key]].append(key)

        res = []

        for i in range(len(arr) - 1, 0, -1):
            for num in arr[i]:
                res.append(num)

                if len(res) == k:
                    return res
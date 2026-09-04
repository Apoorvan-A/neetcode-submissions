class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        count = [False] * 3

        for triplet in triplets:
            i, j, k = triplet

            if i <= target[0] and j <= target[1] and k <= target[2]:
                if i == target[0]:
                    count[0] = True

                if j == target[1]:
                    count[1] = True

                if k == target[2]:
                    count[2] = True

        return all(count)

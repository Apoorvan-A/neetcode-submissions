class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        maxheap=[-stone for stone in stones]
        heapq.heapify(maxheap)
        while maxheap:
            if len(maxheap)==1:
                return -maxheap[0]
            num1=-heapq.heappop(maxheap)
            num2=-heapq.heappop(maxheap)
            if num1!=num2:
                heapq.heappush(maxheap,-abs(num1-num2))
        return 0
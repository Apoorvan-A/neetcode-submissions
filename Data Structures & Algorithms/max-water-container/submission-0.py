class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        res=0
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i == j:
                    continue
                
                area=min(heights[i],heights[j])
                area*=(abs(i-j))

                res=max(res,area)
        return res
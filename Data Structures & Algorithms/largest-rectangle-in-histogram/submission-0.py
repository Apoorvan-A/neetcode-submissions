class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res=0
        stack=[]
        n=len(heights)
        for i in range(n+1):
            curr=heights[i] if i<n else 0
            while stack and heights[stack[-1]]>curr:
                temp=heights[stack.pop()]
                l=stack[-1] if stack else -1
                width=i-l-1
                res=max(res,width*temp)
            stack.append(i)
        return res
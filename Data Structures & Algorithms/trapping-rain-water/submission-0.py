class Solution:
    def trap(self, height: List[int]) -> int:
        
        prefix=[0]*len(height)
        suffix=[0]*len(height)

        prefix[0],suffix[len(height)-1]=0,0
        
        maximum=0
        for i in range(1,len(height)):
            maximum=max(maximum,height[i-1])
            prefix[i]=maximum

        maximum=0
        for i in range(len(height)-2,-1,-1):
            maximum=max(maximum,height[i+1])
            suffix[i]=maximum

        res=0
        
        for i in range(len(height)):
            if(height[i]>prefix[i] or height[i]>suffix[i]):
                continue
            res+=min(prefix[i],suffix[i])-height[i]
        
        return res
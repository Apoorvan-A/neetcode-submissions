class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        curr=set()
        l=0
        r=0
        res=0
        while(r<len(s)):
            while(s[r] in curr):
                curr.remove(s[l])
                l+=1
            curr.add(s[r])
            res=max(res,r-l+1)
            r+=1
                
        return res


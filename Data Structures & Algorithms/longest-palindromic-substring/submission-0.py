class Solution:
    def longestPalindrome(self, s: str) -> str:

        resIdx=0
        reslen=0

        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                if(r-l+1 > reslen):
                    reslen=r-l+1
                    resIdx=l
                l-=1
                r+=1
            
            l,r=i,i+1
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                if(r-l+1 > reslen):
                    reslen=r-l+1
                    resIdx=l
                l-=1
                r+=1
        return s[resIdx:resIdx+reslen]
                
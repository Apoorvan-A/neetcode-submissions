class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=[0]*26
        
        res=0
        l=0
        r=0
        while(r < len(s)):
            count[ord(s[r])-ord("A")]+=1
            currmax=max(count)
            while (((r-l)+1)-currmax) > k:
                count[ord(s[l])-ord("A")]-=1
                currmax=max(count)
                l+=1
            res=max(res,r-l+1)
            r+=1
        return res

                
            

            
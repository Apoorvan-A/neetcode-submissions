class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""   
        have= 0
        l=0
        res=[-1,-1]
        resLen=float('inf')

        count_w={}
        count_t={}

        for ch in t:
            count_t[ch]=count_t.get(ch,0)+1
        need=len(count_t)
        for r in range(len(s)):
            count_w[s[r]]=count_w.get(s[r],0)+1
            if s[r] in count_t and count_t[s[r]]==count_w[s[r]]:
                have+=1
            while have==need :
                if(r-l+1)<resLen:
                    res=[l,r]
                    resLen=r-l+1
                count_w[s[l]]-=1
                if s[l] in count_t and count_t[s[l]] > count_w[s[l]]: 
                    have-=1
                l+=1
        return s[res[0]:res[1]+1] if resLen != float('inf') else ""
                
        
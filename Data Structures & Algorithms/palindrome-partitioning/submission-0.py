class Solution:
    def isplaindrome(self,s):
        l=0
        r=len(s)-1
        while l<=r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        subset=[]
        def backtrack(i,subset):
            if i==len(s):
                res.append(subset.copy())
                return
            for j in range(i,len(s)):
                if  self.isplaindrome(s[i:j+1]):
                    subset.append(s[i:j+1])
                    backtrack(j+1,subset)
                    subset.pop()
        backtrack(0,[])
        return res

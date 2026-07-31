class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=list("".join((s.split())))
        left=0
        right=len(l)-1
        res=True
        while(left<=right):
            if l[left].isalnum()==False:
                left+=1
                continue
            if l[right].isalnum()==False:
                right-=1
            if(l[left].lower()!=l[right].lower()):
                res=False
                break
            else:
                left+=1
                right-=1
        return res
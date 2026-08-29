class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()

        while n!=1:
            if n in seen:
                return False
            temp=n
            new=0
            while temp>0:
                new+=(temp%10)**2
                temp//=10
            seen.add(n)
            n=new

        return True
        

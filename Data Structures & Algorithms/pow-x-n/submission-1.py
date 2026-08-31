class Solution:
    def myPow(self, x: float, n: int) -> float:
        temp=x
        i=0
        '''if n>0:
            while i<n-1:
                temp*=x
                i+=1
            return temp
        elif n<0:
            while i<abs(n-1):
                temp/=x
                i+=1
            return temp
        else:
            return 1'''
        return x**n

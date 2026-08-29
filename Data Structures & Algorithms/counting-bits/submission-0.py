class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for num in range(n+1):
            curr=0
            while num:
                curr+=num&1
                num=num>>1
            res.append(curr)
        return res
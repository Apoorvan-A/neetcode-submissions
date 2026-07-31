class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        leftmin=101
        for price in prices:
            if leftmin>price:
                leftmin=price
            res=max(res,price-leftmin)
        return res
            
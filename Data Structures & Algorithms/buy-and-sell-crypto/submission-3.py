class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP=prices[0]
        maxP=0

        for price in prices:
            
            profit=price-minP
            maxP=max(profit,maxP)
            minP=min(price,minP)
        return maxP




            
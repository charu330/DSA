# 121. Best Time to Buy and Sell Stock


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=1
        profit=0
        maxprofit=0
        while(j<len(prices)):
            if(prices[i]<=prices[j]):
                profit=prices[j]-prices[i]
                maxprofit=max(maxprofit, profit)
                j+=1
            else:
                i=j
                j+=1
        return maxprofit

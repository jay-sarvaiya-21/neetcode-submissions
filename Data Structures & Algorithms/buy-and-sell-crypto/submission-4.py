class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        costprice = prices[0]
        maxProfit = 0
        for price in prices[1:]:
            if price > costprice:
                maxProfit = max(maxProfit,price - costprice)
            else:
                costprice = min(costprice,price)
        return maxProfit

                

        
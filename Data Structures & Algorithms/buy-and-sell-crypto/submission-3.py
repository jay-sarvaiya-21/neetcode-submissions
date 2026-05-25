class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        m_profit,c_profit = 0,0
        cp = prices[0]

        for i in range(len(prices)):
            cp = min(prices[i],cp)
            c_profit = max(prices[i] - cp,0)
            m_profit = max(m_profit,c_profit)
        return m_profit
        
        
        
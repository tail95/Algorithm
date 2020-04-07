class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        buy = 987654321
        sell = 0
        for price in prices:
            if sell > price:
                answer += sell - buy
                buy = price
                sell = 0
            if buy > price:
                buy = price
            if buy < price:
                sell = price
        if sell > buy:
            answer += sell - buy
        return answer
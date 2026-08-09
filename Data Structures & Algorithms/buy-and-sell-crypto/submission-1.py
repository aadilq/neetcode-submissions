class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = res = 0

        for R in range(len(prices)):
            if prices[R] > prices[L]:
                res = max(res, prices[R] - prices[L])
            else:
                L = R
        return res

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0 for _ in range(k+1)] for _ in range(2)] for _ in range(n+1)]
        for idx in range(n-1, -1, -1):
            for buy in range(2):
                for cap in range(1, k+1):
                    if buy == 1:
                        dp[idx][buy][cap] = max(
                            -prices[idx] + dp[idx+1][0][cap],
                            0 + dp[idx+1][1][cap]
                        )
                    else:
                        dp[idx][buy][cap] = max(
                            prices[idx] + dp[idx+1][1][cap-1],
                            0 + dp[idx+1][0][cap]
                        )
        return dp[0][1][k]
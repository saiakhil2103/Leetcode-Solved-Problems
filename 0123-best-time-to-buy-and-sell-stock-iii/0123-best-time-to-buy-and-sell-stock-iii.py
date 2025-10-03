class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]
        # base case: index is n or cap is 0 
        for i in range(n):
            for j in range(2):
                dp[i][j][0] = 0 
        for i in range(2):
            for j in range(3):
                dp[n-1][i][j] = 0 
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range(1, 3):
                    if buy == 1:
                        dp[ind][buy][cap] = max(
                            -prices[ind] + dp[ind+1][0][cap],
                            0 + dp[ind+1][1][cap] 
                        )
                    else:
                        dp[ind][buy][cap] = max(
                            prices[ind] + dp[ind+1][1][cap-1],
                            0 + dp[ind+1][0][cap]
                        )
        return dp[0][1][2]



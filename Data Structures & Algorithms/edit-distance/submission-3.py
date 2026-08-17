class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word2)
        n = len(word1)

        # dp[i][j]: i ranges 0..n (word1 index), j ranges 0..m (word2 index)
        # dp[i][j] = min operations to convert word1[i:] into word2[j:]
        dp = [[0]*(m+1) for _ in range(n+1)]

        # base case: j==m -> word2 exhausted, delete remaining word1[i:]
        for i in range(n+1):
            dp[i][m] = n - i
        # base case: i==n -> word1 exhausted, insert remaining word2[j:]
        for j in range(m+1):
            dp[n][j] = m - j

        # fill backward: dependencies are i+1, j+1 -> larger indices first
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    replace = 1 + dp[i+1][j+1]
                    delete  = 1 + dp[i+1][j]
                    insert  = 1 + dp[i][j+1]
                    dp[i][j] = min(replace, delete, insert)

        return dp[0][0]
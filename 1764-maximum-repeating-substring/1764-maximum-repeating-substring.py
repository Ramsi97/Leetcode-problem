class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n, m = len(sequence), len(word)
        dp = [0]*n
        def match(s):
            return s == word
        for i in range(n):
            l = 0
            for j in range(i, n):
                if sequence[j] != word[(j-i)%m]:
                    break
                l += 1
            dp[i] = l//m
        return max(dp)
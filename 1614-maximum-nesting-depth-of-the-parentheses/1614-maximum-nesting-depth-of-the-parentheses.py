class Solution:
    def maxDepth(self, s: str) -> int:
        
        n, cur = len(s), 0
        result = 0
        for i in range(n):
            if s[i] == "(":
                cur += 1
            elif s[i] == ")":
                cur -= 1
            result = max(result, cur)
        return result
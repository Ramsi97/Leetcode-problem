class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        @cache
        def is_palindrome(left, right):
            if left >= right:
                return True
            return s[left] == s[right] and is_palindrome(left+1, right-1)
        
        @cache
        def dp(index):
            if index >= n:
                return 0

            best = dp(index+1)
            for i in range(k-1, n-index):
                if is_palindrome(index, index+i):
                    best = max(best, dp(index+i+1)+1)
            return best
        
        result = dp(0)
        dp.cache_clear()
        is_palindrome.cache_clear()
        return result
        

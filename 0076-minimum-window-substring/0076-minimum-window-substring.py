class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if Counter(t) - Counter(s):
            return ""
        left = 0
        count_t = Counter(t)
        count_s = Counter()
        ans = s
        for right in range(len(s)):
            count_s[s[right]]+=1
            while left <= right and not count_t - count_s:
                ans = s[left: right+1] if right-left+1 < len(ans) else ans
                count_s[s[left]]-=1
                if not count_s[s[left]]:
                    count_s.pop(s[left])
                left +=1
        return ans
        
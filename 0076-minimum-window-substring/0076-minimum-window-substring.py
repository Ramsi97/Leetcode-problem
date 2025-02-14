class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if Counter(t) - Counter(s):
            return ""
        left = 0
        count_t = Counter(t)
        count_s = Counter()
        ans = [0, len(s)]
        for right in range(len(s)):
            count_s[s[right]]+=1
            while not count_t - count_s:
                ans = [left, right+1] if right-left < ans[1]-ans[0] else ans
                count_s[s[left]]-=1
                if not count_s[s[left]]:
                    count_s.pop(s[left])
                left +=1
        return s[ans[0]: ans[1]]
        
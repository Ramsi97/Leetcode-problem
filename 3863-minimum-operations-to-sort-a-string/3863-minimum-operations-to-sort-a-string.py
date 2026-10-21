class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) == 1 or list(s) == sorted(s):
            return 0
        if len(s) == 2:
            return -1
        cnt = Counter(s)
        # i think the maximum possible answer is 2 or three what is the smallest posible string is last index of the original and the larget one is in the first pos of the original

        sorted_s = sorted(s)
        if s[0] == sorted_s[0] or s[-1] == sorted_s[-1]:
            return 1
        # hundle th 3 case
        if (
            sorted_s[0] == s[-1]
            and sorted_s[-1] == s[0]
            and cnt[s[0]] == 1
            and cnt[s[-1]] == 1
        ):
            return 3
        return 2

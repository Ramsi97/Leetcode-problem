class Solution:
    def balancedString(self, s: str) -> int:

        def windowValid(count, val):
            for key in count:
                if count[key] > val:
                    return False
            return True
        count = Counter(s)
        val = len(s)//4
        if windowValid(count, val):
            return 0
        
        left = 0
        res = len(s)
        for right in range(len(s)):
            count[s[right]] -= 1

            while windowValid(count, val):
                res = min(res, right-left+1)
                count[s[left]] +=1
                left += 1
        return res
        
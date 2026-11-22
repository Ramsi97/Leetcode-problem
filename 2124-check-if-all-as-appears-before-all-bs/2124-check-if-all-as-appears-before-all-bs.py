class Solution:
    def checkString(self, s: str) -> bool:
        if 'b' not in s or 'a' not in s:
            return True
        index = s.index('b')
        for i in range(index,len(s)):
            if s[i] == 'a':
                return False
        return True

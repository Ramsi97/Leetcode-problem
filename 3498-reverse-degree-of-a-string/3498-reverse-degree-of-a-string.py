class Solution:
    def reverseDegree(self, s: str) -> int:
        
        result = 0
        for i, char in enumerate(s):
            result += (i+1)*(26 - ord(char) + 97)
        return result
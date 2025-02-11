class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        result = sorted(s, key = lambda s: int(s[-1]))
        result = [i[:-1] for i in result]
        return " ".join(result)
        
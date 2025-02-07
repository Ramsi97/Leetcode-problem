class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count  = Counter(s)
        return math.floor(count[letter]/len(s)*100)
        
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dic = Counter(chars)
        result = 0
        for word in words:
            if dic > Counter(word):
                result += len(word)
        return result
        
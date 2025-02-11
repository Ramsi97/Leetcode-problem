class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.split()

        text.sort(key = len)
        text = [i.lower() for i in text]
        return " ".join(text).capitalize()
class Solution:
    def reverseVowels(self, s: str) -> str:

        vowel = [char for char in s if char.lower() in ['a', "e", 'i', 'o', 'u']]
        vowel.reverse()
        result = list(s)
        i = 0
        for char in range(len(result)):
            if result[char].lower() in ['a', "e", 'i', 'o', 'u']:
                result[char] = vowel[i]
                i+=1
        return ''.join(result)
                
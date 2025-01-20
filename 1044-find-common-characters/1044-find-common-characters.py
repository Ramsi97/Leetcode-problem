class Solution(object):
    def count(self, word):
        result = [0]*26
        for i in word:
            result[ord(i)-ord('a')]+=1
        return result
    def intersection(self, freq1, freq2):
        return [min(f1,f2) for f1, f2 in zip(freq1, freq2)]
    
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        resultfreq = self.count(words[0])

        for word in words:
            resultfreq = self.intersection(resultfreq, self.count(word))
        
        result = [chr(i + ord('a')) for i in range(len(resultfreq)) for _ in range(resultfreq[i]) if resultfreq[i] != 0]

        return result

        
        

        
        
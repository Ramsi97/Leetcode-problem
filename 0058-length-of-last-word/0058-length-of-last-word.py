class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        j = 0
        while j<len(s) and s[j] == " ":
            j+=1
        i = j

        while i <len(s) and s[i] != " ":
            i+=1
            
        return i-j
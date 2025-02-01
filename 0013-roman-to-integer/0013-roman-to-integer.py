class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        pair  = {"I":1 , "V":5, "X":10, "L":50, "C" : 100, "D" : 500, "M" : 1000 }
        
        result = 0
        for i in range(len(s)-1):
            if ( pair[s[i]] < pair[s[i+1]]):
                result -=  pair[s[i]]
            else:
                result +=pair[s[i]]
        result+=pair[s[-1]]
        return result

        
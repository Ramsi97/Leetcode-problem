class Solution(object):
    def interpret(self, c):
        """
        :type command: str
        :rtype: str
        """
        result = ""
        i = 0
        while i < len(c):
            if( c[i] == "G"):
                result+=c[i]
                i+=1
            elif( c[i] == "(" and c[i+1] == ")"):
                result+="o"
                i+=2
            else:
                result+="al"
                i+=4
        return result
        
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        s = list(s)
        part = list(part)
        i = 0
        while i <= (len(s)- len(part)):
            if s[i:i+len(part)] == part:
                del s[i:i+len(part)]
                i-=len(part)
            i+=1
        return "".join(s)
                
        

        
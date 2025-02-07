class Solution:
    def removeDuplicates(self, s: str) -> str:
        result  = list(s)
        i = 0
        while i < (len(result) - 2):
            if result[i:i+2] == [result[i]]*2:
                result = result[:i] + result[i+2:]
                i-=2
            i+=1
        if result[i:i+2] == [result[i]]*2:
                result = result[:i] + result[i+2:]
                i-=2
        return "".join(result)
            


        
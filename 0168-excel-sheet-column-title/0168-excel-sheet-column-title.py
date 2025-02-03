class Solution:
    def convertToTitle(self, c: int) -> str:
        result = ""

        while c:
            char = c%26
            if char == 0:
                result+="Z"
                c-=1
            else:
                result += chr(ord("A")+char-1)
            c//=26
        return result[::-1]

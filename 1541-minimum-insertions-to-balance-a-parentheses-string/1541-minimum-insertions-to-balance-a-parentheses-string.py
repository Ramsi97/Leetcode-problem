class Solution:
    def minInsertions(self, s: str) -> int:
        
        stack = []
        result = 0
        i = 0
        while i < len(s):
            char = s[i]
            if char == "(":
                stack.append("(")
            else:
                if stack:
                    if i+1 < len(s) and s[i+1] == ")":
                        stack.pop()
                        i += 1
                    else:
                        stack.pop()
                        result += 1
                else:
                    if i+1 < len(s) and s[i+1] == ")":
                        result += 1
                        i += 1
                    else:
                        result += 2
            i += 1
        return result+2*len(stack)
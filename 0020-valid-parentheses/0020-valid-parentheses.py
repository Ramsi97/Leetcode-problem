class Solution:
    def isValid(self, s: str) -> bool:
        
        pair = {"(":")", "{":"}", "[":"]"}

        stack = []
        for char in s:
            if char in pair:
                stack.append(char)
            elif stack and pair[stack[-1]] == char:
                stack.pop()
            else:
                return False
        return not stack

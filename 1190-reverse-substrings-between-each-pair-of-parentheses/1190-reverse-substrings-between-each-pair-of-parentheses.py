class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = [""]
        n = len(s)
        cur = ""
        result = ""
        for char in s:
            if char == "(":
                stack.append("")
            elif char == ")":
                top = stack.pop()
                top = top[::-1]
                stack[-1] += top
            else:
                stack[-1] += char
        return stack[-1]

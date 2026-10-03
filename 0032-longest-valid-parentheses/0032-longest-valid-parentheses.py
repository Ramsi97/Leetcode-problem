class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = []
        result = 0
        for index, par in enumerate(s):
            if stack and par == ')' and s[stack[-1]] == '(':
                stack.pop()
                result = max(result, index - (stack[-1] if stack else -1))
            else:
                stack.append(index)
        return result

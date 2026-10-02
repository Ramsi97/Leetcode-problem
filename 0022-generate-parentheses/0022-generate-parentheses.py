class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(par, i):
            if i+len(par) == 2*n:
                par += ")"*i
                result.add(par)
                return
            
            backtrack(par+"(", i+1)
            if i > 0:
                backtrack(par+")", i-1)
            return
        result = set()
        backtrack("(", 1)
        return list(result)

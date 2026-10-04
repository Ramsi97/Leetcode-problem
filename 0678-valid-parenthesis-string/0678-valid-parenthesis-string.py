class Solution:
    def checkValidString(self, s: str) -> bool:
        

        
        n = len(s)
        @cache
        def dp(index, balance):
            if index == n:
                return not balance
            
            if s[index] == "(":
                return dp(index+1, balance+1)
            elif s[index] == ")":
                if balance > 0:
                    return dp(index+1, balance-1)
                return False
        
            # consider * as (
            opening = dp(index+1, balance+1)
            
            # considering * )
            closing = False
            if balance > 0:
                closing = dp(index+1, balance-1)

            # consider * as empty sting
            empty = dp(index+1, balance)

            return opening or closing or empty
        return dp(0, 0)

            
        

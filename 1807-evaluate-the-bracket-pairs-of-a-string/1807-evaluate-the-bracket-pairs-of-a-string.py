class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        
        pair = dict(knowledge)
        cur = ""
        inbracket = False
        result = []
        n = len(s)
        
        for i in range(n):
            if s[i] == "(":
                inbracket = True
            elif s[i] == ")":
                result.append(pair.get(cur, "?"))
                inbracket = False
                cur = ""
            elif inbracket:
                cur += s[i]
            else:
                result.append(s[i])
        return "".join(result)

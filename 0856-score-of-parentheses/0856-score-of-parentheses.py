class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        n = len(s)
        def score(left, right):
            if left >= right:
                return 0.5
            cnt = 0
            index = []
            for i in range(left, right+1):
                if s[i] == "(":
                    cnt += 1
                else:
                    cnt -= 1
                if cnt == 0:
                    index.append(i)
            prev = left
            result = 0
            for end in index:
                result += 2*score(prev+1, end-1)
                prev = end+1
            return result
        return int(score(0, n-1))

                

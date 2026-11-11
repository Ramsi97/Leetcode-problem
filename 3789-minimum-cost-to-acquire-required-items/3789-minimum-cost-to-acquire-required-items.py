class Solution:
    def minimumCost(self, a: int, b: int, c: int, x: int, y: int) -> int:
        
        # lets calculate separately
        if a+b <= c:
            return a*x + b*y
        
        elif c < a and c < b:
            return max(x, y)*c
        elif c < a:
            return x*c + max(0, y-x)*b
        elif c < b:
            return y*c + max(0, x-y)*a
        return min(x, y)*c + max(0, x-y)*a + max(0, y-x)*b


            

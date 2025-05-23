class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x,y = 0, 0

        for char in moves:
            if char == "U":
                y+=1
            elif char == "D":
                y -=1
            elif char == "R":
                x += 1
            else:
                x -= 1
        return x == 0 and y == 0
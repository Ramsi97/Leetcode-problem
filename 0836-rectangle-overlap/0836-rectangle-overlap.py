class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        left = rec1[2] <= rec2[0]
        right = rec1[0] >= rec2[2]
        up = rec1[1] >= rec2[3]
        down = rec1[3] <= rec2[1]
        return not(left or  right or up or down)
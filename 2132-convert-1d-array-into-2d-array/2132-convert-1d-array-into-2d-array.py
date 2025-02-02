class Solution(object):
    def construct2DArray(self, o, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if m*n != len(o):
            return []

        result = []
        k = 0
        for i in range(m):
            col = []
            for j in range(n):
                col.append(o[k])
                k+=1
            result.append(col)
        return result
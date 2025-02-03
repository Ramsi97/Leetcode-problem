class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """

        lose = {}
        for w,l in matches:
            lose[l] = lose.get(l,0) + 1
        set1 = set()
        for i in matches:
            set1.update(i)

        result = [[],[]]
        for i in set1:
            if(lose.get(i, 0) == 0):
                result[0].append(i)
            elif lose[i] == 1:
                result[1].append(i)
        result[0].sort()
        result[1].sort()

        return result
        
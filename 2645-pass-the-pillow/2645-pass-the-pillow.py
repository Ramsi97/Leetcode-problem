class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        current = 1
        direction = 0
        for i in range(time):

            if current == n or current == 1:
                direction +=1

            if direction%2 == 0:
                current -= 1
            else:
                current += 1
        return current
        
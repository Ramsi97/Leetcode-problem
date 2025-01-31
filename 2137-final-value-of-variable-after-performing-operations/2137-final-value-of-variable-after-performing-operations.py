class Solution(object):
    def finalValueAfterOperations(self, o):
        """
        :type operations: List[str]
        :rtype: int
        """
        result = 0
        for i in o:
            if i == "--X" or i == "X--":
                result-=1
            else:
                result+=1
        return result
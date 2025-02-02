class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed = set(allowed)
        result = sum(1 for i in words if set(i).issubset(allowed))
        return result
        
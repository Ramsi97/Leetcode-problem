class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        strs.sort()
        l =len(strs[0])
        for i in range(l):
            c = strs[0][i]
            for j in range(len(strs)):
                if c != strs[j][i]:
                    return result
            result+=c
        return result

        
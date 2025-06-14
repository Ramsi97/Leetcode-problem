class Solution:
    def minMaxDifference(self, num: int) -> int:
        k = str(num)
        for i in range(len(k)):
            if k[i] != "9":
                break
        max_ = k
        if i != len(k):
            max_ = int(k.replace(k[i], "9"))

        min_ = int(k.replace(k[0], "0"))
        return max_ - min_

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        n = len(s)
        last_index = {}
        for i in range(n):
            last_index[s[i]] = i
        print(last_index)
        left = 0
        right = 0
        result = []
        end = 0
        while right < n:
            end = max(end, last_index[s[right]])
            print(right, last_index[s[right]])
            if right == end:
                print(s[i])
                result.append(right-left+1)
                left = right+1
            right+=1
        return result
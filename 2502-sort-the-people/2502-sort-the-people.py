class Solution:
    def sortPeople(self, names: List[str], height: List[int]) -> List[str]:

        size = len(names)

        for i in range(size):
            mx = i
            for j in range(i, size):
                if height[mx] < height[j] :
                    mx = j
            height[mx], height[i] = height[i], height[mx]
            names[mx], names[i] = names[i], names[mx]

        return names
        
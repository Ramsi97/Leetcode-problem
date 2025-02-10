class Solution:
    def sortPeople(self, names: List[str], height: List[int]) -> List[str]:

        n= len(names)
        sortted = True
        for i in range(n):
            for j in range(n-i - 1):
                if height[j] < height[j+1]:
                    sortted = False
                    height[j+1], height[j] = height[j], height[j+1]
                    names[j+1], names[j] = names[j], names[j+1]
            if sortted:
                break

        return names
                    
        
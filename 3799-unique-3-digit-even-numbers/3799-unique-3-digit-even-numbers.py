class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        result = set()
        for a, b, c in list(permutations(digits, 3)):
            if a != 0 and not c%2:
                result.add((a,b,c))
        return len(result)
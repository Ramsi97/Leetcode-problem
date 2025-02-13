class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        tree =  defaultdict(int)
        n = len(fruits)
        left = 0
        result = 0
        ans = 0
        for right in range(n):
            tree[fruits[right]]+=1
            result += 1
            while len(tree) > 2:
                tree[fruits[left]] -= 1
                if not tree[fruits[left]]:
                    tree.pop(fruits[left])
                result -= 1 
                left += 1
            ans  = max(ans, result)
        return ans
            
            
        
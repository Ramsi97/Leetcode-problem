class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        result = [0]*n
        queue = deque(range(n))
        r = 0
        for i in range(n-1):
            result[queue[0]] = deck[r]
            r += 1
            queue.popleft()
            l = queue.popleft()
            queue.append(l)
        result[queue[0]] = deck[r]
        return result

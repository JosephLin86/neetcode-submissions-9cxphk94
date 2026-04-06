class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        small, large = 1, max(piles)
        result = 0
        while small < large:
            counter = 0
            middle = (small + large) // 2
            for pile in piles:
                counter += math.ceil(float(pile) / middle)
            
            if counter > h:
                small = middle + 1
            else:
                large = middle
                result = middle
        return small

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)

        res = max(piles)

        while L <= R:
            mid = (L + R) // 2

            hrs = 0
            for bananaPile in piles:
                hrs += math.ceil(bananaPile / mid)
            if hrs <= h:
                res = mid
                R = mid - 1
            else:
                L = mid + 1
        return res


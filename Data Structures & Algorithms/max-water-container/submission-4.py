class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
         0 1 2 3 4 5 6 7
        [1,7,2,5,4,7,3,6]
        '''
        L, R = 0, len(heights) - 1

        res = 0

        while L < R:
            currWater = max(res, (R - L) * min(heights[L], heights[R]))
            res = max(res, currWater)

            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1
        return res
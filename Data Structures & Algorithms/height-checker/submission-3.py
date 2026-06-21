class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        countArr = [0] * 101

        for height in heights:
            countArr[height] += 1
        

        expected = []

        for h in range(1, 101):
            if countArr[h] == 0:
                continue
            c = countArr[h]
            for _ in range(c):
                expected.append(h)
        res = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1
        return res
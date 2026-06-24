class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        print(len(grid) ** 2)
        countArr = [0] * ((len(grid) ** 2) + 1)


        for pair in grid:
            for num in pair:
                countArr[num] += 1
        print(countArr)

        double = missing = 0
        for i in range(1, len(countArr)):
            if countArr[i] == 2:
                double = i
            if countArr[i] == 0:
                missing = i
        return [double, missing]



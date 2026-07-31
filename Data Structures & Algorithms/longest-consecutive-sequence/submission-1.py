class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        numset = set(nums)

        maxLength = 1

        for num in numset:
            if num - 1 not in numset:
                currentLength = 1
                currentNum = num
                while currentNum + 1 in numset:
                    currentLength += 1
                    currentNum += 1
                maxLength = max(maxLength, currentLength)
        return maxLength



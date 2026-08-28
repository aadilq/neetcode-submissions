class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        L = 0

        for R in range(len(nums)):
            if nums[R] % 2 == 0:
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
        return nums
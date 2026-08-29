class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        print(k)

        L, R = 0, len(nums) - 1

        while L < R:
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
            R -= 1
        print(nums)

        L, R = 0, k - 1
        while L < R:
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
            R -= 1
        
        L, R = k, len(nums) - 1
        while L < R:
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
            R -= 1

        
        
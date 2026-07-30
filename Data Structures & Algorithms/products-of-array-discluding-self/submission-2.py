class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        prefixP = 1
        for i in range(len(nums)):
            output[i] = prefixP
            prefixP *= nums[i]
        print(output)

        postfixP = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfixP
            postfixP *= nums[i]
        return output
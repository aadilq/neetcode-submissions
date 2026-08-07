class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dailyTemps = [0] * (len(temperatures))

        stack = []

        for index, temperature in enumerate(temperatures):
            ## if there is a number in the stack and its greater than the previous number on the stack
            while stack and temperature > stack[-1][1]:
                idx, tmp = stack.pop()
                dailyTemps[idx] = index - idx
            else:
                stack.append([index, temperature])
        return dailyTemps





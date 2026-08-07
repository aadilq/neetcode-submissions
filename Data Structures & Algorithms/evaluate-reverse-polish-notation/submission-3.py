class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char in "+*/-":
                if char == "+":
                    num1, num2 = stack.pop(), stack.pop()
                    stack.append(num1 + num2)
                if char == "*":
                    num1, num2 = stack.pop(), stack.pop()
                    stack.append(num1 * num2)
                if char == "-":
                    num1, num2 = stack.pop(), stack.pop()
                    stack.append(num2 - num1)
                if char == "/":
                    num1, num2 = stack.pop(), stack.pop()
                    stack.append(int(num2 / num1))
            else:
                stack.append(int(char))
        return stack[0]

class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ")": "(", 
            "]": "[",
            "}": "{"
        }

        stack = []

        for character in s:
            ## if it's a closing character
            if character in closeToOpen:
                if stack and stack[-1] == closeToOpen[character]:
                    stack.pop()
                else:
                    return False
            ## if it's a opening character
            else:
                stack.append(character)
        return not stack
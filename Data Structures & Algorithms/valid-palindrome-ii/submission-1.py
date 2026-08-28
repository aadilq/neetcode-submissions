class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindromeCheck(s, L, R):
            while L < R:
                if s[L] != s[R]:
                    return False
                L += 1
                R -= 1
            return True
    
        L, R = 0, len(s) - 1

        while L < R:
            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                return (palindromeCheck(s, L + 1, R) or
                         palindromeCheck(s, L, R - 1))
        return True

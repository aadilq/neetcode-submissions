class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}

        L = res = 0

        for R in range(len(s)):
            charCount[s[R]] = 1 + charCount.get(s[R], 0)
            while (R - L + 1) - max(charCount.values()) > k:
                charCount[s[L]] -= 1
                L += 1
            res = max(res, (R - L + 1))
        return res
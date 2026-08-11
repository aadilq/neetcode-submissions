class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        tcount = {}

        for char in t:
            tcount[char] = tcount.get(char, 0) + 1
        
        have, need = 0, len(tcount)
        res, reslen = "", float('inf')
        scount = {}
        L = 0

        for R in range(len(s)):
            char = s[R]
            
            scount[char] = scount.get(char, 0) + 1

            if char in tcount and scount[char] == tcount[char]:
                have += 1
            
            while have == need:
                if R - L + 1 < reslen:
                    reslen = R - L + 1
                    res = s[L:R+1]
                scount[s[L]] -= 1
                if s[L] in tcount and scount[s[L]] < tcount[s[L]]:
                    have -= 1
                L += 1
        return res if reslen != float('inf') else ""
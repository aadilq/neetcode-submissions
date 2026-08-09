class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1count, s2count = {}, {}

        for i in range(len(s1)):
            s1count[s1[i]] = 1 + s1count.get(s1[i], 0)
            s2count[s2[i]] = 1 + s2count.get(s2[i], 0)
        if s1count == s2count:
            return True
        
        L = 0 

        for R in range(len(s1), len(s2)):
            s2count[s2[L]] -= 1
            if s2count[s2[L]] == 0:
                del s2count[s2[L]]
            L += 1
            s2count[s2[R]] = 1 + s2count.get(s2[R], 0)
            if s1count == s2count:
                return True
        return False
        
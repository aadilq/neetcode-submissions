from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount = defaultdict(int)

        for letter in s:
            scount[letter] += 1
        
        for letter in t:
            if letter not in scount:
                return False
            scount[letter] -= 1
            if scount[letter] == 0:
                del scount[letter]
        return len(scount) == 0

        
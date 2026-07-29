from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramList = defaultdict(list)

        for word in strs:
            letterCount = [0] * 26
            for letter in word:
                letterCount[ord(letter) - ord('a')] += 1
            anagramList[tuple(letterCount)].append(word)
        return list(anagramList.values())
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabetical = [26] * 26
        subtract = 0
        for letter in order:
            alphabetical[ord(letter) - ord('a')] -= subtract
            subtract += 1
        print(alphabetical)

        for word in range(len(words) - 1):
            word1, word2 = words[word], words[word + 1]

            for j in range(len(word1)):
                if j == len(word2):
                    return False
                if word1[j] != word2[j]:
                    if alphabetical[ord(word1[j]) - ord('a')] < alphabetical[ord(word2[j]) - ord('a')]:
                        return False
                    break
        return True

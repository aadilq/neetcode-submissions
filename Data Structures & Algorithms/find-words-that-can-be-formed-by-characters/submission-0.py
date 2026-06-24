class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charscheck = Counter(chars)

        res = 0

        for word in words:
            cur_word = defaultdict(int)
            good = True
            for c in word:
                cur_word[c] += 1
                if c not in charscheck or cur_word[c] > charscheck[c]:
                    good = False
            if good:
                res += len(word)
        return res




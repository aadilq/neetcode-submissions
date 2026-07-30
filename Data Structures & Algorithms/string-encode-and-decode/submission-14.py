class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string += str(len(word)) + '#' + word
        return string

    def decode(self, s: str) -> List[str]:
        '''
        5#Hello5#Word
        i
         j
        '''
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            wordlen = int(s[i:j])
            res.append(s[j + 1: j + 1 + wordlen])
            i = j + 1 + wordlen
        return res

            

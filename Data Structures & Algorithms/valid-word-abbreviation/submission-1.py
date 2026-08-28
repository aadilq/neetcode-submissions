class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        i = j = 0

        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isalpha() or abbr[j] == "0":
                return False
            else:
                sublength_str = ""
                while j < len(abbr) and not abbr[j].isalpha():
                    sublength_str += abbr[j]
                    j += 1
                sublength = int(sublength_str)
                i += sublength
        return i == len(word) and j == len(abbr)
                
            
            



        
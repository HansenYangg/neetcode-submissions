class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
      

        while i < len(word) and j < len(abbr):

            print(abbr[j], i, j)
            if abbr[j].isdigit():
                if abbr[j] == "0":
                    return False
             
                digits = ""
                while j < len(abbr) and abbr[j].isdigit():
                        digits += abbr[j]
                        j += 1

                digits = int(digits)
             
                while i < len(word) and digits > 0:
                    i += 1
                    digits -= 1
                    
                if digits:
                    
                    return False

            else:
                
                if word[i] != abbr[j]:
                    return False
                i, j = i + 1, j + 1


        return i == len(word) and j == len(abbr)



        
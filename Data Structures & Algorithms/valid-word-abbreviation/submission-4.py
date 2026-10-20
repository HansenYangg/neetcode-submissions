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

                if i + int(digits) > len(word):
                    
                    return False

                i += int(digits)

            else:
                
                if word[i] != abbr[j]:
                    return False
                i, j = i + 1, j + 1


        return i == len(word) and j == len(abbr)



        
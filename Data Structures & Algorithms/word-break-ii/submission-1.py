class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        res, wordDict = [], set(wordDict)
    
        def backtrack(sentence, word, chars, i):
            if i == len(s) and chars == len(s):
                res.append(sentence)
                return 
            
            if i >= len(s):
                return 

            for end in range(i + 1, len(s) + 1):
                word = s[i:end]
                if word in wordDict: 
                    if sentence:
                        backtrack(sentence + " " + word, "", chars + len(word), end )
                    else:
                        backtrack(word, "", chars + len(word), end )
                

        backtrack("", "", 0, 0)
        return res

    
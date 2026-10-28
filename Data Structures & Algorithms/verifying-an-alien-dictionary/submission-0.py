class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        mapping = { order[i]: i + 1 for i in range(len(order)) }
        

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            for i in range(len(word1)):
                if i == len(word2) or mapping[word1[i]] > mapping[word2[i]]:
                    return False
                elif mapping[word1[i]] < mapping[word2[i]]:
                    break
                

                



        return True


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

        

    def addWord(self, word: str) -> None:
        
        curr = self.root
       
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.endOfWord = True

            
        

    def search(self, word: str) -> bool:

        def helper(word, trie):

            for idx, char in enumerate(word):
                if char == ".":
                    for child in trie.children:
                        if helper(child + word[idx + 1:], trie):
                            return True
                    return False

                else:
                    if char not in trie.children:
                        return False

                    trie = trie.children[char]

            return trie.endOfWord


        return helper(word, self.root)













        

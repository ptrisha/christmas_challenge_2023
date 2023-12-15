# Day 15 of Leetcode Problem
# Problem description:
# https://leetcode.com/problems/implement-trie-prefix-tree

class TrieNode:
    def __init__(self):
        # Children refer to 26 lowercase letters in the alphabet
        self.children = [None]*26
        # End of word marker
        self.isEOW = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # an internal function to find the index of the letter
    def _getIndex(self, ch):
        return ord(ch) - ord('a')
        
    def insert(self, word: str) -> None:

        levelNode = self.root
        for level, letter in enumerate(word):
            index = self._getIndex(letter)
            if not levelNode.children[index]:
                levelNode.children[index]= TrieNode()

            levelNode = levelNode.children[index]

        # mark the end of the word
        levelNode.isEOW = True



    def search(self, word: str) -> bool:
        levelNode = self.root
        for level, letter in enumerate(word):
            index = self._getIndex(letter)
            if not levelNode.children[index]:
                return False
            levelNode = levelNode.children[index]
        return levelNode.isEOW

        
        

    def startsWith(self, prefix: str) -> bool:
        levelNode = self.root
        for level, letter in enumerate(prefix):
            index = self._getIndex(letter)
            if not levelNode.children[index]:
                return False
            levelNode = levelNode.children[index]
        return True

        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

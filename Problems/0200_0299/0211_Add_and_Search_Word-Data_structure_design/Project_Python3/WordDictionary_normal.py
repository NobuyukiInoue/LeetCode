import re

class WordDictionary:
    # Time Limit Exceeded.

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = []

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if word not in self.words:
            self.words.append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if "." not in word:
            if word in self.words:
                return True
            else:
                return False
        else:
            for w in self.words:
                if re.match(word, w) and len(word) == len(w):
                    return True
            return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

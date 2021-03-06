class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if len(word) not in self.dict:
            self.dict[len(word)] = [word]
        else:
            self.dict[len(word)].append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if len(word) not in self.dict:
            return False

        if '.' not in word:
            return word in self.dict[len(word)]

        for x in self.dict[len(word)]:
            for i in range(len(x)):
                if x[i] != word[i] and word[i] != '.':
                    break
            else:
                return True

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

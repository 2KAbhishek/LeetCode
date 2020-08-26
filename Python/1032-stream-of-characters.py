class StreamChecker:

    def __init__(self, words):
        T = lambda: collections.defaultdict(T)
        self.trie = T()
        for w in words: reduce(dict.__getitem__, w[::-1], self.trie)['#'] = True
        self.S = ""
        self.W = max(map(len, words))

    def query(self, letter):
        self.S = (letter + self.S)[:self.W]
        cur = self.trie
        for c in self.S:
            if c in cur:
                cur = cur[c]
                if cur['#'] == True:
                    return True
            else:
                break
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

class Node:
    def __init__(self):
        self.chars = {}
        self.word = False

class Trie:
    def __init__(self):
        self.node = Node()

    def add_word(self, word):
        node = self.node
        for c in word:
            if c not in node.chars:
                node.chars[c] = Node()
            node = node.chars[c]
        node.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie()
        for word in words:
            trie.add_word(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, trie.node, res, "", i, j)
        return res

    def dfs(self, board, trie, res, word, i, j):
        if trie.word:
            res.append(word)
            trie.word = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if not trie:
            return
        char = board[i][j]
        if char in trie.chars:
            board[i][j] = '#'
            trie = trie.chars[char]
            for x, y in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
                self.dfs(board, trie, res, word + char, i + x, y + j)
            board[i][j] = char

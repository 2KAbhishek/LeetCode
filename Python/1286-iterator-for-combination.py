class CombinationIterator:
    
    def __init__(self, characters: str, combinationLength: int):
        self.combinations = list(map("".join, itertools.combinations(characters, r=combinationLength)))

    def next(self) -> str:
        return self.combinations.pop(0)

    def hasNext(self) -> bool:
        if self.combinations:
            return True
        return False

#     def __init__(self, characters: str, combinationLength: int):
#         self.characters = characters
#         self.n = len(characters)
#         self.combinations = gen_combinations(self.n, combinationLength)
#         self.ind = len(self.combinations) - 1

#     def next(self) -> str:
#         s = ""
#         for i in range(self.n):
#             if self.combinations[self.ind][i] != "0":
#                 s += self.characters[i]
#         self.ind -= 1
#         return s

#     def hasNext(self) -> bool:
#         return self.ind > -1 
    
# def gen_combinations(l, n):
#     end = int("1" * l, 2)
#     ans = []
#     for i in range(end + 1):
#         b = bin(i)[2:]
#         if b.count('1') == n:
#             ans.append(b.zfill(l))
#     return ans


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
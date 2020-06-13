class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []
        self.lookup = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.lookup:
            return False
        self.lookup[val] = len(self.items)
        self.items.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not val in self.lookup:
            return False
        self.items[self.lookup[val]] = self.items[-1] # set last element at index of val
        self.lookup[self.items[-1]] = self.lookup[val] # set last elements index as index of val
        self.items.pop()
        del self.lookup[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.items)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
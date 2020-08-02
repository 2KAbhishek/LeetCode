class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = set()

    def add(self, key: int) -> None:
        self.list.add(key)


    def remove(self, key: int) -> None:
        if key in self.list:
            self.list.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.list



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

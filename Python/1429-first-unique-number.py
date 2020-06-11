class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = collections.deque()
        self.lookup = {}

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if len(self.queue) == 0:
            return -1
        while len(self.queue) > 0 and self.queue[0] in self.lookup and self.lookup[self.queue[0]] >=2:
            self.queue.popleft()
        if len(self.queue) == 0:
            return -1
        return self.queue[0]


    def add(self, value: int) -> None:
        if value in self.lookup:
            self.lookup[value] += 1
        else: self.lookup[value] = 1

        self.queue.append(value)



# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

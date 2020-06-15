class MedianFinder:
    # Time Limit Exceeded.

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.length = 0

    def addNum(self, num: int) -> None:
        self.length += 1
        if self.length == 1:
            self.data.append(num)
        elif self.length == 2:
            if num > self.data[0]:
                self.data.append(num)
            else:
                self.data = [num] + self.data[:]
        else:
            if num <= self.data[0]:
                self.data = [num] + self.data[:]
                return
            for i in range(self.length - 1):
                if num <= self.data[i]:
                    self.data = self.data[:i] + [num] + self.data[i:]
                    return
            self.data.append(num)

    def findMedian(self) -> float:
        if self.length % 2 == 1:
            return self.data[self.length // 2]
        else:
            mid = (self.length + 1) // 2
            return (self.data[mid - 1] + self.data[mid]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

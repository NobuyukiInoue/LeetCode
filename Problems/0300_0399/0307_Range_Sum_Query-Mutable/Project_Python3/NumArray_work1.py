class NumArray:
#   def __init__(self, nums: List[int]):
    def __init__(self, nums):
        self.list = nums

#   def update(self, i: int, val: int) -> None:
    def update(self, i, val):
        self.list[i] = val

#   def sumRange(self, i: int, j: int) -> int:
    def sumRange(self, i, j):
        sum = 0
        for n in range(i, j + 1):
            sum += self.list[n]
        return sum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

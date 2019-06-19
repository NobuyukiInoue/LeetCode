class NumArray:
#   def __init__(self, nums: List[int]):
    def __init__(self, nums):
        # 736ms
        self.update = nums.__setitem__
        self.sumRange = lambda i, j: sum(nums[i:j + 1])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

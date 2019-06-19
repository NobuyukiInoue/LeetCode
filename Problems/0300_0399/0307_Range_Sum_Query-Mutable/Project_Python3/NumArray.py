class NumArray:
    # 92ms

#   def __init__(self, nums: List[int]):
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.array = [0]*(self.n + 1)
        for i in range(self.n):
            self.helper(i, nums[i])

    def helper(self,i, val):
        n = self.n
        i += 1
        while i <= n:
            self.array[i] += val
            i += i & (-i)
            
#   def update(self, i: int, val: int) -> None:
    def update(self, i, val):
        self.helper(i, val - self.nums[i])
        self.nums[i] = val
        
#   def sumRange(self, i: int, j: int) -> int:
    def sumRange(self, i, j):
        sum_i = self.get_sum(i - 1)
        sum_j = self.get_sum(j)
        return sum_j - sum_i
        
    def get_sum(self, i):        
        s = 0
        i += 1
        while i > 0:
            s += self.array[i]
            i -= i & (-i)
        return s

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

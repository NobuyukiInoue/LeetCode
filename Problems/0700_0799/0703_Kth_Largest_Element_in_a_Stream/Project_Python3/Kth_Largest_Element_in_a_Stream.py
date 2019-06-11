import os
import sys
import time
import heapq

class KthLargest:
#   def __init__(self, k: int, nums: List[int]):
    def __init__(self, k, nums):
        self.res = []
        self.k = k
        for i in nums:
            if len(self.res) < k:
                heapq.heappush(self.res,i)
            else:
                heapq.heappushpop(self.res,i)

#   def add(self, val: int) -> int:
    def add(self, val):
        if len(self.res) < self.k:
            heapq.heappush(self.res,val)
        else:
            heapq.heappushpop(self.res,val)
        return self.res[0]

"""
#   def __init__(self, k: int, nums: List[int]):
    def __init__(self, k, nums):
        self.k = k - 1
        nums.sort()
        self.list = nums[::-1]

#   def add(self, val: int) -> int:
    def add(self, val):
        if len(self.list) == 0:
            self.list = [val]
        else:
            for i in range(len(self.list) - 1):
                if val > self.list[i]:
                    self.list = self.list[0:i] + [val] + self.list[i:]
                    break
                elif i == len(self.list) - 1:
                    self.list = self.list + [val]
                    break
        
        if self.k >= len(self.list):
            return None
        else:
            return self.list[self.k]
"""

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

class Solution:
    def calc(self, cmds, args):
        for i in range(len(cmds)):
            if cmds[i] == "KthLargest":
                flds = args[i].replace("]", "").split(",[")
                k = int(flds[0]) 
                if len(flds[1]) == 0:
                    nums = []
                else:
                    nums = [int(val) for val in flds[1].split(",")]
                Kth = KthLargest(k, nums)
                print("Execute kthLargest()")
            else:
                if Kth == None:
                    print("cmd not found... %s" %cmds[i])
                    exit(1)
                elif cmds[i] == "add":
                    print("Kth.add(%s) = %s" %(args[i], Kth.add(int(args[i]))))
                else:
                    print("error... %s" %cmds[i])
                    exit(1)

def main():
    argv = sys.argv
    argc = len(argv)

    if (argc < 2):
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()


def loop_main(temp):
    flds = temp.replace(" ","").replace("\"","").replace("]]]","").rstrip().split("],[[")
    cmds = flds[0].replace("[[","").split(",")
    args = flds[1].split("],[")

    print("cmds[] = %s" %cmds)
    print("args[] = %s" %args)

    time0 = time.time()

    sl = Solution()
    sl.calc(cmds, args)

    time1 = time.time()


    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()

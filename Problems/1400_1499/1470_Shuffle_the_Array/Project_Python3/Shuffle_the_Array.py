import os
import sys
import time

class Solution:
#   def shuffle(self, nums: List[int], n: int) -> List[int]:
    def shuffle(self, nums, n):
        # 60ms
        return [b for a in zip(nums[:n], nums[n:]) for b in a]

    def shuffle2(self, nums, n):
        # 60ms
        res = [0 for _ in nums]
        mid = len(nums)//2
        for i in range(mid):
            res[2*i] = nums[i]
            res[2*i + 1] = nums[mid + i]
        return res

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python {0} <testdata.txt>".format(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("{0} not found...".format(argv[1]))
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    nums = [int(val) for val in str_args[0].split(",")]
    n = int(str_args[1])
    print("nums[] = {0}, n = {1:d}".format(nums, n))

    sl = Solution()
    time0 = time.time()
    result = sl.shuffle(nums, n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

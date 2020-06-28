import os
import sys
import time

class Solution:
#   def findNumbers(self, nums: List[int]) -> int:
    def findNumbers(self, nums):
        # 48ms
        return len([i for i in nums if len(str(i)) % 2 == 0])

    def findNumbers_work(self, nums):
        # 48ms
        result = 0
        for target in nums:
            if len(str(target)) % 2 == 0:
                result += 1
        return result

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
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip()

    nums = [int(val) for val in flds.split(",")]
    print("nums1 = {0}".format(nums))

    sl = Solution()
    time0 = time.time()
    result = sl.findNumbers(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

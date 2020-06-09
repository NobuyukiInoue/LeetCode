import collections
import os
import sys
import time

class Solution:
#   def largestNumber(self, nums: List[int]) -> str:
    def largestNumber(self, nums: List[int]) -> str:
        # 36ms
        return str(int(''.join(sorted(map(str, nums), key=lambda s:s*9)[::-1])))

    def largestNumber2(self, nums):
        # 40ms
        nums = list(map(str, nums))
        m = max([len(n) for n in nums])
        nums = sorted(nums, key=lambda n: n * (m // len(n) + 1), reverse=True)
        return str(int(''.join(nums)))

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
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
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    nums = [int(val) for val in flds.split(",")]
    print("nums = {0}".format(nums))

    time0 = time.time()

    sl = Solution()
    result = sl.largestNumber(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))


if __name__ == "__main__":
    main()

import os
import sys
import time

class Solution:
#    def pivotIndex(self, nums: List[int]) -> int:
    def pivotIndex(self, nums):
        # two passes
        if len(nums) <= 2:
            return -1
        
        s = sum(nums)
        leftsum = 0
        for i in range(0, len(nums)):
            # print(leftsum)
            if leftsum * 2 + nums[i] == s:
                return i
            leftsum += nums[i]
        return -1

#    def pivotIndex(self, nums: List[int]) -> int:
    def pivotIndex2(self, nums):
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1

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
    str_args = temp.replace(" ","").replace("\"","").replace("[","").replace("]","").rstrip()

    nums = [int(n) for n in str_args.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()
    time0 = time.time()
    result = sl.pivotIndex(nums)


    time1 = time.time()
    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

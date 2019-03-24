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

def str_to_int_array(flds):
    if len(flds) <= 0:
        return None
    temp = flds.split(",")
    nums = [0]*len(temp)
    for i in range(len(temp)):
        nums[i] = int(temp[i])
    return nums

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
    str_args = temp.replace(" ","").replace("\"","").replace("[","").replace("]","").rstrip()
    nums = str_to_int_array(str_args)
    print("nums[] = %s" %nums)

    time0 = time.time()

    sl = Solution()
    result = sl.pivotIndex(nums)

    print("result = %d" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()

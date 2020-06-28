import os
import sys
import time
from collections import deque

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        all_nums = nums1 + nums2
        all_nums.sort()
        all_nums_length = len(all_nums)

        if len(all_nums) % 2 == 1:
            result = all_nums[all_nums_length // 2]
        else:
            result = (all_nums[all_nums_length // 2 - 1] + all_nums[all_nums_length // 2])/2.0

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    nums1 = [int(val) for val in flds[0].split(",")]
    nums2 = [int(val) for val in flds[1].split(",")]
    print("nums1 = {0}, nums2 = {1}".format(nums1, nums2))

    sl = Solution()
    time0 = time.time()

    result = sl.findMedianSortedArrays(nums1, nums2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

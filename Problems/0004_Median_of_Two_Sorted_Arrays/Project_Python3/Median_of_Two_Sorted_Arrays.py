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
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()


def loop_main(temp):
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    nums1 = str_to_int_array(flds[0])
    nums2 = str_to_int_array(flds[1])

    time0 = time.time()

    sl = Solution()
    result = sl.findMedianSortedArrays(nums1, nums2)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()

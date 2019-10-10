# coding: utf-8

import os
import sys
import time
import math

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1=set(nums1)
        nums2=set(nums2)
        return list(nums1&nums2)

    def intersection_work1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result_num = []

        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if nums2[i] in result_num:
                    continue
                if nums2[i] == nums1[j]:
                    result_num.append(nums2[i])
        
        return result_num

    def intersection_work_bad(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result_index = [0]*len(nums2)
        count = 0

        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if i in result_index:
                    continue
                if nums2[i] == nums1[j]:
                    result_index[count] = i
                    count += 1
        
        result_nums = [0]*count
        for i in range(0, count):
            result_nums[i] = nums2[result_index[i]]
        
        return result_nums

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
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    flds = temp.replace("[[","").replace("]]","").rstrip().split("],[")
    nums1 = flds[0].split(",")
    nums2 = flds[1].split(",")

    print("nums1 = %s, nums2 = %s" %(nums1, nums2))

    time0 = time.time()

    sl = Solution()
    result = sl.intersection(nums1, nums2)
    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()

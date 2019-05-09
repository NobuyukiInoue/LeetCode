# coding: utf-8

import os
import sys
import time

class Solution:
#    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def nextGreaterElement(self, nums1, nums2):
        cache, st = {}, []
        for x in nums2:
            if len(st) == 0:
                st.append(x)
            elif x <= st[-1]:
                st.append(x)
            else:
                while st and st[-1] < x:
                    cache[st.pop()] = x
                st.append(x)
        result = []
        for x in nums1:
            if x in cache:
                result.append(cache[x])
            else:
                result.append(-1)
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
        temp = temp.strip()
        if temp == "":
            continue
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    flds = temp.replace("\"","").replace(" ","").replace("[[","").replace("]]","").rstrip().split("],[")
    list1 = str_to_int_array(flds[0])
    list2 = str_to_int_array(flds[1])

    print("list1 = %s" %list1)
    print("list2 = %s" %list2)

    time0 = time.time()

    sl = Solution()
    result = sl.nextGreaterElement(list1, list2)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()

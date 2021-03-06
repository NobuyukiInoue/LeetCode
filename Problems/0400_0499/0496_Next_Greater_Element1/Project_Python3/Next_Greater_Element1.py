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
    flds = temp.replace("\"","").replace(" ","").replace("[[","").replace("]]","").rstrip().split("],[")

    list1 = [int(val) for val in flds[0].split(",")]
    list2 = [int(val) for val in flds[1].split(",")]
    print("list1 = {0}".format(list1))
    print("list2 = {0}".format(list2))

    sl = Solution()
    time0 = time.time()

    result = sl.nextGreaterElement(list1, list2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

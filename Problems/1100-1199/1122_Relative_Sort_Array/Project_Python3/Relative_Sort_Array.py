# coding: utf-8

import os
import sys
import time

class Solution:
#   def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    def relativeSortArray(self, arr1, arr2):
        # 36ms
        k = {v: i for i, v in enumerate(arr2)}
        return sorted(arr1, key=lambda i: k.get(i, 1000 + i))

    def relativeSortArray_work(self, arr1, arr2):
        # 64ms
        pos = 0
        for target in arr2:
            for i in range(pos, len(arr1)):
                if arr1[i] == target:
                    if i != pos:
                        temp = arr1[pos]
                        arr1[pos] = arr1[i]
                        arr1[i] = temp
                    pos += 1
        leastlist = arr1[pos:]
        leastlist.sort()
        return arr1[:pos] + leastlist

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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")

    arr1 = [int(n) for n in flds[0].split(",")]
    arr2 = [int(n) for n in flds[1].split(",")]
    print("arr1 = {0}, arr2 = {1}".format(arr1, arr2))

    time0 = time.time()

    sl = Solution()
    result = sl.relativeSortArray(arr1, arr2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

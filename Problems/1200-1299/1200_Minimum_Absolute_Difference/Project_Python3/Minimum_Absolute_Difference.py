# coding: utf-8

import os
import sys
import time

class Solution:
#   def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:        
    def minimumAbsDifference(self, arr):
        arr.sort()
        val_min = sys.maxsize
        for i in range(len(arr) - 1):
            val_sub = arr[i + 1] - arr[i]
            if val_sub < val_min:
                val_min = val_sub
        results = []
        for i in range(len(arr) -  1):
            val_sub = arr[i + 1] - arr[i]
            if val_sub == val_min:
                results.append([arr[i], arr[i + 1]])
        return results

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    arr = [int(n) for n in flds.split(",")]
    print("arr = {0}".format(arr))

    time0 = time.time()

    sl = Solution()
    result = sl.minimumAbsDifference(arr)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

# coding: utf-8

import collections
import os
import sys
import time

class Solution:
#   def checkIfExist(self, arr: List[int]) -> bool:
    def checkIfExist(self, arr):
        # 44ms
        lst = set()
        for num in arr:
            if 2*num in lst or num%2 == 0 and num // 2 in lst:
                return True
            lst.add(num)
        return False

    def checkIfExist2(self, arr):
        # 52ms
        lst = []
        for num in arr:
            if 2*num in lst or num%2 == 0 and num // 2 in lst:
                return True
            lst.append(num)
        return False

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    arr = [int(n) for n in flds.split(",")]
    print("arr = {0}".format(arr))

    time0 = time.time()

    sl = Solution()
    result = sl.checkIfExist(arr)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

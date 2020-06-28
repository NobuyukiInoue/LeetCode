# coding: utf-8

import os
import sys
import time

class Solution:
#   def duplicateZeros(self, arr: List[int]) -> None:
    def duplicateZeros(self, arr):
        # 76ms
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 1
            i += 1

    def duplicateZeros2(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        # 96ms
        if not arr or len(arr) < 1:
            return
        
        zero_count = arr.count(0)
        p_short, p_long = len(arr) - 1, len(arr) + zero_count - 1
        while p_short >= 0:
            if arr[p_short] != 0:
                if p_long < len(arr):
                    arr[p_long] = arr[p_short]
            else:
                if p_long < len(arr):
                    arr[p_long] = 0
                p_long -= 1
                if p_long < len(arr):
                    arr[p_long] = 0
                    
            p_short -= 1
            p_long -= 1

    #   def duplicateZeros(self, arr: List[int]) -> None:
    def duplicateZeros_work(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                subarr = arr[i:len(arr) - 1]
                arr = arr[:i]
                arr.append(0)
                arr += subarr
                i += 2
            else:
                i += 1
        print("result = {0}".format(arr))

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")
    arr = [int(num) for num in flds]
    print("arr = {0}".format(arr))

    sl = Solution()
    time0 = time.time()
    sl.duplicateZeros(arr)

    time1 = time.time()

    print("result = {0}".format(arr))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

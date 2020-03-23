# coding: utf-8

import collections
import os
import sys
import time

class Solution:
#   def sortByBits(self, arr: List[int]) -> List[int]:
    def sortByBits(self, arr):
        # 64ms
       return sorted(arr, key=lambda a: [bin(a).count('1'), a])

    def sortByBits2(self, arr):
        # 80ms
        arr.sort()
        len_arr = len(arr)
        maxBits, temp = 0, arr[len_arr - 1]

        while temp > 0:
            temp >>= 1
            maxBits += 1
        table = [[0 for _ in range(0)] for _ in range(maxBits)]

        for i in range(len_arr):
            table[self.countBits(arr[i])].append(arr[i])

        res = []
        for i in range(len(table)):
            res += table[i]

        return res

    def countBits(self, num):
        count = 0
        while num > 0:
            if num % 2 == 1:
                count += 1
            num >>= 1
        return count

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
    result = sl.sortByBits(arr)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

# coding: utf-8

import json
import os
import sys
import time

class Solution:
#   def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
    def containsPattern(self, arr, m, k):
        # 28ms
        streak = 0
        for i in range(len(arr) - m):
            streak = streak + 1 if arr[i] == arr[i + m] else 0
            if streak == (k - 1)*m:
                return True
        return False

    def containsPattern2(self, arr, m, k):
        # 36ms
        i = 0
        while i <= len(arr) - 1:
            p = arr[i : i + m]
            if p * k == arr[i : i + m*k]:
                return True
            i += 1
        return False

    def containsPattern_bad(self, arr, m, k):
        arr_str = "".join(map(str, arr))
        searched_str = {}
        for i in range(len(arr_str) - m):
            target_pattern = arr_str[i:i+m]
            if target_pattern in searched_str:
                continue
            searched_str[target_pattern] = 1
            count = 1
            for j in range(i + m, len(arr_str)):
                if target_pattern in arr_str[j:]:
                    count += 1
                    if count >= k:
                        return True
        return False

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    arr, m, k = [int(n) for n in flds[0].split(",")], int(flds[1]), int(flds[2])
    print("arr = {0}, m = {1}, k = {2}".format(arr, m, k))

    sl = Solution()
    time0 = time.time()

    result = sl.containsPattern(arr, m, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

import collections
import heapq
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        # 31ms
        res = []
        for i in range(len(nums) - k + 1):
            c = [[count, val] for val, count in collections.Counter(nums[i:i + k]).items()]
            c = heapq.nlargest(x, c)
            res.append(sum(val * count for count, val in c))
        return res

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    
    num, k, x = [int(num) for num in flds[0].split(",")], int(flds[1]), int(flds[2])
    print("num = {0}, k = {1:d}, x = {2:d}".format(num, k, x))

    sl = Solution()
    time0 = time.time()

    result = sl.findXSum(num, k, x)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

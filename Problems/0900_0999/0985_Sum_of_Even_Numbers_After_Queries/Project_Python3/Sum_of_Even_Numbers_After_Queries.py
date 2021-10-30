# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # 512ms
        even_sum = sum(a for a in nums if a % 2 == 0)
        ans = []
        for query in queries:
            val, index = query
            even_sum -= nums[index] % 2 == 0 and nums[index]
            nums[index] += val
            even_sum += nums[index] % 2 == 0 and nums[index]
            ans.append(even_sum)
        return ans

    def sumEvenAfterQueries2(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # 502ms
        even_sum = sum(a for a in nums if a % 2 == 0)
        for i, query in enumerate(queries):
            val, index = query
            even_sum -= nums[index] % 2 == 0 and nums[index]
            nums[index] += val
            even_sum += nums[index] % 2 == 0 and nums[index]
            queries[i] = even_sum
        return queries

    def sumEvenAfterQueries3(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # 516ms
        even_sum = sum(num for num in nums if num%2 == 0)
        ans = []
        for val, index in queries:
            if nums[index]%2 == 0 and val%2 == 0:
                even_sum += val
                nums[index] += val
            elif nums[index]%2 != 0 and val%2 != 0:
                nums[index] += val
                even_sum += nums[index]
            elif nums[index]%2 == 0:
                even_sum -= nums[index]
                nums[index] += val
            else:
                nums[index] += val
            ans.append(even_sum)
        return ans

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
    flds = temp.replace(" ", "").replace("\"", "").rstrip().split("],[[")

    nums = [int(n) for n in flds[0].replace("[", "").split(",")]
    flds1 = flds[1].replace("]]]", "").split("],[")
    if len(flds1[0]) == 0:
        queries = []
    else:
        queries = [[int(col) for col in data.split(",")] for data in flds1]
    print("nums = {0}, queries = {1}".format(nums, queries))

    sl = Solution()
    time0 = time.time()

    result = sl.sumEvenAfterQueries(nums, queries)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

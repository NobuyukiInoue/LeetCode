import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        # 732ms - 752ms
        diagonals = []
        for i, num in enumerate(nums):
            if i != -(i + 1):
                diagonals.append(num[i])
                diagonals.append(num[-(i + 1)])
            else:
                diagonals.append(num[i])
        diagonals.sort(reverse=True)
        for diag in diagonals:
            if self.isPrime(diag):
                return diag
        return 0

    def isPrime(self, n) -> bool:
        if n == 1:
            return False
        if n == 2 or n == 3:
            return True
        limit = int(math.sqrt(n))
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while limit - i >= 0:
            if n % i == 0:
                return False
            i += 2
        return True

    def diagonalPrime_2liner(self, nums: List[List[int]]) -> int:
        # 1152ms - 1165ms
        def p(n, i = 2): return (n > 1)*n if i*i > n else p(n, i + 1) if n % i else 0
        return max([max(p(nums[i][i]), p(nums[len(nums) - 1 - i][i])) for i, num in enumerate(nums)])

def printGrid(title, grid):
    print("{0} = [".format(title))
    for i, _ in enumerate(grid):
        if i == 0:
            print(" [", end = "")
        else:
            print(",[", end = "")
        for j in range(len(grid[i])):
            if j == 0:
                print("{0:d}".format(grid[i][j]), end = "")
            else:
                print(",{0:d}".format(grid[i][j]), end = "")
        print("]")
    print("]")

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    
    nums = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    printGrid("nums", nums)

    sl = Solution()
    time0 = time.time()

    result = sl.diagonalPrime(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

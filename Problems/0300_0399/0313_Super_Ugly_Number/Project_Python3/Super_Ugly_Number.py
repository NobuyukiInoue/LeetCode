# coding: utf-8

import os
import sys
import time

class Solution:
#   def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
    def nthSuperUglyNumber(self, n, primes):
        # 360ms
        nums = [1]*len(primes)
        idx = [0]*len(primes)
        best = [1]
        cur = 1
        for i in range(n - 1):
            for j in range(len(idx)):
                if nums[j] == cur:
                    nums[j] = best[idx[j]]*primes[j]
                    idx[j] += 1
            cur = min(nums)
            best.append(cur)
        return best[-1]

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

    n = int(flds[0])
    primes = [int(n) for n in flds[1].split(",")]
    print("n = {0:d}, K = {1}".format(n, primes))

    time0 = time.time()

    sl = Solution()
    result = sl.nthSuperUglyNumber(n, primes)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

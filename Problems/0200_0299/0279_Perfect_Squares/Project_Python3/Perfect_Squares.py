import math
import os
import sys
import time

class Solution:
#   def numSquares(self, n: int) -> int:
    def numSquares(self, n: int) -> int:
        # 4064ms
        limit = int(math.sqrt(n)) + 1
        dp = [i for i in range(n + 1)]
        for i in range(1, limit):
            sqi = i ** 2
            for j in range(sqi, n + 1):
                dp[j] = min(dp[j], 1 + dp[j - sqi])
        return dp[n]

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
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()


def loop_main(temp):
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    n = int(flds)
    print("n = {0:d}".format(n))

    time0 = time.time()

    sl = Solution()
    result = sl.numSquares(n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))


if __name__ == "__main__":
    main()

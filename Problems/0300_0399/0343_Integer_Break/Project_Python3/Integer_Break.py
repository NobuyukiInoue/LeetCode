import os
import sys
import time

class Solution:
#   def integerBreak(self, n: int) -> int:
    def integerBreak(self, n):
        # 28ms
        return n - 1 if n < 4 else 3**((n - 2)//3)*((n - 2)%3 + 2)

    def integerBreak2(self, n):
        # 24ms
        if n == 2:
            return 1
        if n == 3:
            return 2
        if (n - 2) % 3 == 0:
            return 3**((n - 2)//3)*2
        if (n - 3) % 3 == 0:
            return 3**((n-3)//3)*3
        if (n - 4) % 3 == 0:
            return 3**((n-4)//3)*4

    def integerBreak3(self, n):
        # 40ms
        dp = [0, 0, 1]
        for i in range(3, n + 1):
            dp.append(0)
            for j in range(i):
                dp[i] = max(dp[i], max(dp[i - j], i - j)*max(dp[j], j))     
        return dp[n]

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
    fld = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    n = int(fld)
    print("n = {0:d}".format(n))

    sl = Solution()
    time0 = time.time()

    result = sl.integerBreak(n)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

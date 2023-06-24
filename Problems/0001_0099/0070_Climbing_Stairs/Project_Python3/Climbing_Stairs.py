import os
import sys
import time

class Solution:
    def climbStairs0(self, n: int) -> int:
        # 42ms - 48ms
        prev, prev2 = 1, 0
        for _ in range(1, n + 1):
            curi = prev + prev2
            prev2 = prev
            prev = curi
        return prev

    def climbStairs1(self, n: int) -> int:
        # 51ms
        dp = [0] + [1] + [2] + [0] * (n - 2)
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    def climbStairs(self, n: int) -> int:
        # 38ms - 43ms
        resultArray = [-1]*(n + 1)

        def calc_next(n: int) -> int:
            if resultArray[n] >= 0:
                return resultArray[n]
            total = 0
            for i in range(1, 3):
                if i == n:
                    total += 1
                    break
                if i > n:
                    break
                total += calc_next(n - i)
            resultArray[n] = total
            return total

        return calc_next(n)


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
    flds = temp.replace(", ", ",").replace("\"", "").replace("[", "").replace("]", "").rstrip()

    n = int(flds)
    print("n = {0:d}".format(n))

    sl = Solution()
    time0 = time.time()

    result = sl.climbStairs(n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

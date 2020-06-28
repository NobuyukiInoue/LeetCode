import os
import sys
import time

class Solution:
#   def minimumDeleteSum(self, s1: str, s2: str) -> int:
    def minimumDeleteSum(self, s1, s2):
        # 544ms
        len1, len2, total  = len(s1), len(s2), 0
        num1 = [ord(i) for i in s1]
        num2 = [ord(i) for i in s2]
        total = sum(num1 + num2)
        dpMatrix = [[None]*(len2 + 1) for i in range(len1 + 1)]
        for i in range(len1 + 1):
            for j in range(len2 + 1):
                if i == 0 or j == 0:
                    dpMatrix[i][j] = 0
                elif num1[i - 1] == num2[j - 1]:                       
                    dpMatrix[i][j] = dpMatrix[i - 1][j - 1] + num1[i - 1]
                else:
                    if dpMatrix[i - 1][j] > dpMatrix[i][j - 1]: 
                        dpMatrix[i][j] = dpMatrix[i - 1][j]
                    else: 
                        dpMatrix[i][j] = dpMatrix[i][j - 1]
        return total - 2*dpMatrix[len1][len2]

    def minimumDeleteSum2(self, s1, s2):
        # 1080ms
        len1, len2 = len(s1), len(s2)
        MAX = sys.maxsize
        dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        for i in range(len1, -1, -1):
            for j in range(len2, -1, -1):
                if i < len1 or j < len2:
                    if i < len1 and j < len2 and ord(s1[i]) == ord(s2[j]):
                        dp[i][j] = dp[i + 1][j + 1]
                    else:
                        if i < len1:
                            t1 = ord(s1[i]) + dp[i + 1][j]
                        else:
                            t1 = MAX
                        if j < len2:
                            t2 = ord(s2[j]) + dp[i][j + 1]
                        else:
                            t2 = MAX
                        dp[i][j] = min(t1, t2)
        return dp[0][0]

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
        print("argv[1] = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    flds = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")

    s1, s2 = flds[0], flds[1]
    print("s1 = {0}, s2 = {1}".format(s1, s2))

    sl = Solution()
    time0 = time.time()
    result = sl.minimumDeleteSum(s1, s2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

import collections
import os
import sys
import time

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 40ms
        self.dic = collections.defaultdict(set)
        TS = set(t)
        for i, c in enumerate(s):
            if c in TS:
                self.dic[c].add(i)
        return sum(self.search(t).values())

    def search(self, t):
        resDic = collections.defaultdict(int)
        if len(t) == 1:
            for x in self.dic[t[0]]:
                resDic[x] = 1
        else:
            for index, count in self.search(t[0:-1]).items():
                for a in self.dic[t[-1]]:
                    if a > index:
                        resDic[a]+=count
        return resDic

    def numDistinct2(self, s: str, t: str) -> int:
        # 148ms
        dp = [[1] * (len(s)+1)] + [[0] * (len(s)+1) for y in range(len(t))]
        for j in range(1, len(t)+1):
            for i in range(1, len(s)+1):
                if s[i-1] == t[j-1]:
                    dp[j][i] += dp[j-1][i-1] + dp[j][i-1]
                else:
                    dp[j][i] = dp[j][i-1]
        return dp[-1][-1]

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
    words = temp.replace(", ",",").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    s, t = words[0], words[1]

    print("s = \"{0}\", t = \"{1}\"".format(s, t))

    sl = Solution()
    time0 = time.time()
    result = sl.numDistinct(s, t)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

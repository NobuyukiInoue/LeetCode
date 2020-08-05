# coding: utf-8

import collections
import os
import sys
import time

class Solution:
#   def leastInterval(self, tasks: List[str], n: int) -> int:
    def leastInterval(self, tasks, n):
        # 420ms
        freq = collections.Counter(tasks)
        Most_freq = freq.most_common()[0][1]
        Found_most = sum([freq[key] == Most_freq for key in freq])
        return max(len(tasks), (Most_freq - 1) * (n + 1) + Found_most)

    def leastInterval2(self, tasks, n):
        # 432ms
        if tasks == None or len(tasks) == 0:
            return 0
        cnt = [0]*(ord('Z') - ord('A') + 1)
        for ch in tasks:
            cnt[ord(ch) - ord('A')] += 1
        cnt.sort()
        maxCnt = cnt[25] -1
        spaces = maxCnt*n
        for i in range(24, -1, -1):
            spaces -= min(maxCnt, cnt[i])
        spaces = max(0, spaces)
        return len(tasks) + spaces

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
    tasks, n = [ch for ch in flds[0].split(",")], int(flds[1])
    print("tasks = {0}, n = {1:d}".format(tasks, n))

    sl = Solution()
    time0 = time.time()

    result = sl.leastInterval(tasks, n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

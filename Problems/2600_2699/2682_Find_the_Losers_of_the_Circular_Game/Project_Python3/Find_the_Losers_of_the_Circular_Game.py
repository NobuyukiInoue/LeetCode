import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # 65ms - 74ms
        check = [False for _ in range(n)]
        i, pre = 1, 0
        while not check[pre]:
            check[pre] = True
            pre = (i*k + pre)%n
            i += 1
        ans = []
        for i in range(1, n):
            if not check[i]:
                ans.append(i + 1)
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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    n, k  = int(flds[0]), int(flds[1])
    print("n = {0:d}, k = {1:d}".format(n, k))

    sl = Solution()
    time0 = time.time()

    result = sl.circularGameLosers(n, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countAndSay(self, n: int) -> str:
        # 41ms - 66ms
        if n == 1:
            return "1"
        x = self.countAndSay(n - 1)
        ans, y, ct = "", x[0], 1
        for i in range(1, len(x)):
            if x[i] == y:
                ct += 1
            else:
                ans += str(ct) + str(y)
                y, ct = x[i], 1
        ans += str(ct) + str(y)
        return ans

    def countAndSay2(self, n: int) -> str:
        # 76ms - 83ms
        if n < 1 and n > 30:
            return ""
        data = []
        data.append("1")
        for _ in range(1, n):
            temp = ""
            pos = 0
            while pos < len(data[-1]):
                count = self.count_continuity_num(data[-1], pos)
                temp += str(count) + data[-1][pos]
                pos += count
            data.append(temp)
        return data[n - 1]

    def count_continuity_num(self, data: str, pos: int) -> int:
        i, count = 0, 0
        while pos + i < len(data):
            if data[pos + i] == data[pos]:
                count += 1
            else:
                return count
            i += 1
        return count
 
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

    result = sl.countAndSay(n)

    time1 = time.time()

    print("result = \"{0}\"".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

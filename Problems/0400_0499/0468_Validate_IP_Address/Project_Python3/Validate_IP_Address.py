import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        # 31ms - 38ms
        def isIPv4(s: str) -> bool:
            try:
                return str(int(s)) == s and 0 <= int(s) <= 255
            except:
                return False

        def isIPv6(s: str) -> bool:
            try:
                return len(s) <= 4 and int(s, 16) >= 0
            except:
                return False

        if queryIP.count(".") == 3 and all(isIPv4(flds) for flds in queryIP.split(".")):
            return "IPv4"
        if queryIP.count(":") == 7 and all(isIPv6(flds) for flds in queryIP.split(":")):
            return "IPv6"
        return "Neither"

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
    queryIP = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    print("queryIP = \"{0}\"".format(queryIP))

    sl = Solution()
    time0 = time.time()

    result = sl.validIPAddress(queryIP)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

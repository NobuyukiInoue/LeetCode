import re
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        # 0ms
        left_part, right_part = p.split("*")
        left_idx = s.find(left_part)
        right_idx = s.find(right_part, left_idx + len(left_part))
        return left_idx != -1 and right_idx != -1

    def hasMatch2(self, s: str, p: str) -> bool:
        # 20ms - 26ms
        return re.findall(p.replace('*', '.*'), s) != []

    def hasMatch3(self, s: str, p: str) -> bool:
        # 0ms - 2ms
        n = len(s)
        parts = p.split("*")
        prefix, suffix = parts[0], parts[1]
        p_len, s_len = len(prefix), len(suffix)
        prefix_found = True if len(prefix) == 0 else False
        suffix_found = True if len(suffix) == 0 else False
        i = 0
        while i < n - s_len + 1:
            if not prefix_found and s[i:i + p_len] == prefix:
                prefix_found = True
                i += p_len
                continue
            elif prefix_found and s[i:i + s_len] == suffix:
                suffix_found = True
                break
            i += 1
        return prefix_found and suffix_found

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
    flds = temp.replace("[", "").replace("]", "").replace("\"", "").replace(", ", ",").rstrip().split(",")
    
    s, p = flds[0], flds[1]
    print("s = \"{0}\", p = \"{1}\"".format(s, p))

    sl = Solution()
    time0 = time.time()

    result = sl.hasMatch(s, p)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

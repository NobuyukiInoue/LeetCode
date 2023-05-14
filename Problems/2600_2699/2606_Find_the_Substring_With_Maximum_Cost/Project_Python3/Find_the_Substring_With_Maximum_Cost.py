import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        # 175ms - 176ms
        char_dict = {}
        for i, ch in enumerate(chars):
            char_dict[ch] = vals[i]
        max_cost = 0
        curr_cost = 0
        for i, ch in enumerate(s):
            if ch not in char_dict:
                curr_cost += ord(ch) - 96
            else:
                curr_cost += char_dict[ch]
            if curr_cost < 0:
                curr_cost = 0
            if curr_cost > max_cost:
                max_cost = curr_cost
        return max_cost

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
    flds = temp.replace(", ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    s, chars = flds[0], flds[1]
    vals = [int(num) for num in flds[2].split(",")]
    print("s = \"{0}\", chars = \"{1}\", vals = {2}".format(s, chars, vals))

    sl = Solution()
    time0 = time.time()

    result = sl.maximumCostSubstring(s, chars, vals)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

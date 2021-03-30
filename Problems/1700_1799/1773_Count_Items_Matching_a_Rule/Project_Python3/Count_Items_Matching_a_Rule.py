import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countMatche2(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # 224ms
        idx = ["type", "color", "name"].index(ruleKey)
        return sum(item[idx] == ruleValue for item in items)

    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # 232ms
        res, col = 0, 0
        if ruleKey == "type":
            col = 0
        elif ruleKey == "color":
            col = 1
        elif ruleKey == "name":
            col = 2
        for item in items:
            if ruleValue == item[col]:
                res += 1
        return res

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
    flds = temp.replace(", ",",").replace("\"","").replace("[[[","").rstrip().split("]],[")

    items = [[data for data in item.split(",")] for item in flds[0].split("],[")]
    flds1 = flds[1].replace("]]", "").split("],[")
    ruleKey, ruleValue = flds1[0], flds1[1]
    print("items = {0}".format(items))
    print("ruleKey = {0}, ruleValue = {1}".format(ruleKey, ruleValue))

    sl = Solution()
    time0 = time.time()

    result = sl.countMatches(items, ruleKey, ruleValue)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

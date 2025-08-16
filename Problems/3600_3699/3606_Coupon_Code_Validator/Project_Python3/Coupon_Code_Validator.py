import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        # 4ms - 11ms
        ans = []
        dic =  collections.defaultdict(int, {"electronics": 1, "grocery":2, "pharmacy":3, "restaurant":4})
        data = list(zip(code, businessLine, isActive))
        data.sort(key = lambda x:(dic[x[1]], x[0]))
        for coup_id, bus_cat, cur_act in data:
            if not coup_id.replace('_', 'a').isalnum():
                continue
            if dic[bus_cat] == 0:
                continue
            if not cur_act:
                continue
            ans.append(coup_id)
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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    
    code = flds[0].split(",")
    businessLine = flds[1].split(",")
    isActive = flds[2].split(",")
    print("code = {0}, businessLine = {1}, isActive = {2}".format(code, businessLine, isActive))

    sl = Solution()
    time0 = time.time()

    result = sl.validateCoupons(code, businessLine, isActive)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

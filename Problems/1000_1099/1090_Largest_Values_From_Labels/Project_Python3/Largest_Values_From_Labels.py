import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        # 110ms - 117ms
        used_count = collections.defaultdict(int)
        ans = 0
        for val, label in sorted(zip(values, labels), reverse=True):
            if not numWanted:
                break
            if used_count[label] >= useLimit:
                continue
            used_count[label] += 1
            numWanted -= 1
            ans += val
        return ans

    def largestValsFromLabels_slow(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        # 6864ms - 6878ms
        n = len(values)
        dic = {}
        for i in range(n):
            if not labels[i] in dic:
                dic[labels[i]] = []
            dic[labels[i]].append(values[i])
        for k, v in dic.items():
            dic[k].sort(reverse=True)
            if len(v) > useLimit:
                dic[k] = dic[k][:useLimit]
        ans = 0
        while numWanted > 0:
            max_value_label, max_value = -1, 0
            for k, v in dic.items():
                if len(v) == 0:
                    continue
                if v[0] > max_value:
                    max_value_label = k
                    max_value = v[0]
            if max_value_label == -1:
                break
            ans += dic[max_value_label][0]
            dic[max_value_label] = dic[max_value_label][1:]
            numWanted -= 1
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
    
    values = [int(num) for num in flds[0].split(",")]
    labels = [int(num) for num in flds[1].split(",")]
    numWanted, useLimit = int(flds[2]), int(flds[3])
    print("values = {0}, labels = {1}, numWanted = {2:d}, useLimit = {3:d}".format(values, labels, numWanted, useLimit))

    sl = Solution()
    time0 = time.time()

    result = sl.largestValsFromLabels(values, labels, numWanted, useLimit)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

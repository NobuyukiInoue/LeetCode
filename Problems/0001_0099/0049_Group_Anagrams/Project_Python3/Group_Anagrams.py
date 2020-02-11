# coding: utf-8

import collections
import itertools
import os
import sys
import time

class Solution:
#   def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    def groupAnagrams(self, strs):
        # 96ms
        sortedstrs = [''.join(sorted(s)) for s in strs]
        freq = collections.defaultdict(list)
        for i in range(len(strs)):
            freq[sortedstrs[i]] += strs[i],
        res = []
        for _, v in freq.items():
            res += v,
        return res

    def groupAnagrams2(self, strs):
        # 116ms
	    return [sorted(g) for _, g in itertools.groupby(sorted(strs, key=sorted), sorted)]

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    strs = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    print("strs = {0}".format(strs))

    time0 = time.time()

    sl = Solution()
    result = sl.groupAnagrams(strs)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

# coding: utf-8

import os
import sys
import time
#from collections import defaultdict
import collections

class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        cnt = collections.defaultdict(list)
        for i in range(len(points) - 1):
            for j in range(i+1, len(points)):
                dist = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                cnt[dist].append(set([i, j]))
        for same in cnt.values():
            for i in range(len(same) - 1):
                for j in range(i + 1, len(same)):
                    if same[i] & same[j]:
                        ans += 2
        return ans

def str_to_2int_array(flds):
    if len(flds) <= 0:
        return None
    points = [[0]*2]*len(flds)

    points = [[0 for j in range(2)] for i in range(len(flds))]
    for i in range(len(flds)):
        temp = flds[i].split(",")
        points[i][0] = int(temp[0])
        points[i][1] = int(temp[1])
    return points

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
    var_str = temp.replace("[[","").replace("]]","").rstrip()
    flds = var_str.split("],[")
    points = str_to_2int_array(flds)

    sl = Solution()
    time0 = time.time()
    result = sl.numberOfBoomerangs(points)

    print("result = {0}".format(result))

    time1 = time.time()
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

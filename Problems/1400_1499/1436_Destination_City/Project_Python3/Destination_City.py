# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def destCity(self, paths: List[List[str]]) -> str:
    def destCity(self, paths):
        # 48ms
        dic = {}
        res = ""
        for i in range(len(paths)):
            dic[paths[i][0]] = paths[i][0]
        for i in range(len(paths)):
            if paths[i][1] not in dic.keys():
                res = paths[i][1]
                break
        return res

    def destCity2(self, paths):
        # 52ms
        A, B = map(set, zip(*paths))
        return (B - A).pop()

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip()

    paths = [[col for col in data.split(",")] for data in flds.split("],[")]
    print("paths = {0}".format(paths))
  
    time0 = time.time()

    sl = Solution()
    result = sl.destCity(paths)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

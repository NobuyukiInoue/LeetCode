# coding: utf-8

import os
import sys
import time

class Solution:
#    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
    def numberOfLines2(self, widths, S):
        if len(S) <= 0:
            return [0, 0]
        length = 0
        for i in range(len(S)):
            length += widths[ord(S[i]) - ord("a")]
        
        return [length // 100 + 1, length % 100]

    def numberOfLines(self, widths, S):
        res, cur = 1, 0
        for i in S:
            width = widths[ord(i) - ord('a')]
            if cur + width > 100:
                res += 1
            if cur + width > 100:
                cur = width
            else:
                cur += width
        return [res, cur]


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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")
    str_widths = flds[0].split(",")

    widths = [0] * len(str_widths)
    for i in range(len(str_widths)):
        widths[i] = int(str_widths[i])
    S = flds[1]

    print("widths = %s" %widths)
    print("S = %s" %S)

    time0 = time.time()

    sl = Solution()
    result = sl.numberOfLines(widths, S)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()

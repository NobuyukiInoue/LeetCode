# coding: utf-8

import os
import sys
import time

class Solution:
    #def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    def nextGreatestLetter(self, letters, target) -> str:
        if not letters:
            return "a"
        l = 0
        r = len(letters)-1
        while (l<r-1):
            mid = (l+r)//2
            if (letters[mid]<= target):
                l = mid+1
            else:
                r = mid
        if letters[l] > target:
            return letters[l]
        elif letters[r] > target:
            return letters[r]
        else:
            return letters[0]

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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")

    letters = flds[0].split(",")
    target = flds[1]
    print("letters = {0}".format(letters))
    print("target = {0}".format(target))

    sl = Solution()
    time0 = time.time()

    result = sl.nextGreatestLetter(letters, target)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

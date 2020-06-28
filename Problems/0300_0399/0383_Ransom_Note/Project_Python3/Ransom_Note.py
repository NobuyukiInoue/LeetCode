# coding: utf-8

import os
import sys
import time

class Solution:
#    def canConstruct(self, ransomNote: 'str', magazine: 'str') -> 'bool':
    def canConstruct(self, ransomNote, magazine):
        for x in ransomNote:
            idx = magazine.find(x)
            if idx == -1:
                return False
            magazine = magazine[0:idx]+magazine[idx+1:]
                
        return True

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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").rstrip().split("],[")

    ransomNote = flds[0]
    magazine = flds[1]
    print("ransomNote = {0}".format(ransomNote))
    print("magazine = {0}".format(magazine))

    sl = Solution()
    time0 = time.time()

    result = sl.canConstruct(ransomNote, magazine)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

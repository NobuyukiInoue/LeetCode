# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

from NestedInteger.NestedInteger import NestedInteger
from NestedInteger.NestedIterator import NestedIterator

class Solution:
    def NestedIteratorExecute(self, flds: List[List[int]]) -> List[int]:
        nestedList = self.setNestedIterator(flds)
        return self.getNestedIterator(nestedList)

    def setNestedIterator(self, flds: List[List[int]]) -> List[NestedInteger]:
        nestedInteger = []
        for fld in flds:
            nestedInteger.append(NestedInteger(fld))
        return nestedInteger

    def getNestedIterator(self, nestedList: List[NestedInteger]) -> List[int]:
        i, v = NestedIterator(nestedList), []
        while i.hasNext():
            v.append(i.next())
        return v

def strToListIntArray(flds_str: str) -> List[int]:
    flds = []
    if flds_str[0] == "[" and flds_str[-1] == "]":
        flds_str = flds_str[1:-1]
    while flds_str != "":
        if flds_str[0] == "]":
            return flds
        if flds_str[0] == ",":
            flds_str = flds_str[1:]
        if flds_str[0] == "[":
            flds_str = flds_str[1:]
            end_pos, depth = 0, 1
            while depth > 0:
                if flds_str[end_pos] == "[":
                    depth += 1
                elif flds_str[end_pos] == "]":
                    depth -= 1
                end_pos += 1
            flds.append(strToListIntArray(flds_str))
            flds_str = flds_str[end_pos + 1:]
        else:
            pos1 = flds_str.find(",")
            pos2 = flds_str.find("]")
            if pos1 == -1 and pos2 == -1:
                flds.append(int(flds_str))
                flds_str = ""
            elif pos2 >= 0:
                if pos2 < pos1 or pos1 == -1:
                    flds.append(int(flds_str[:pos2]))
                    return flds
                else:
                    flds.append(int(flds_str[:pos1]))
                    flds_str = flds_str[pos1+1:]
            elif pos1 >= 0:
                flds.append(int(flds_str[:pos1]))
                flds_str = flds_str[pos1+1]
            else:
                print("Error")
    return flds

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
    flds_str = temp.replace(", ",",").rstrip()
    flds = strToListIntArray(flds_str)
    print("flds = {0}".format(flds))

    time0 = time.time()

    sl = Solution()
    result = sl.NestedIteratorExecute(flds)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

import collections
import os
import sys
import string
import time
from typing import List, Dict, Tuple

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 104ms
        if endWord not in wordList:
            return []
        front, back = {beginWord: [[beginWord]]}, {endWord: [[endWord]]}
        fwords, ewords = set(wordList), set(wordList)
        while front and back:
            if len(front) > len(back):
                front, back = back, front
                fwords, ewords = ewords, fwords
            hold = collections.defaultdict(list)
            toDel, res = set(), []
            for wd, pths in front.items():
                nxts = fwords & {wd[:i] + c + wd[i + 1:] \
                        for i in range(len(wd)) for c in string.ascii_lowercase}
                toDel |= nxts
                for w in nxts:
                    for pth in pths:
                        if w in back:
                            if pth[0] == beginWord:
                                res += [pth + bk[::-1] for bk in back[w]]
                            else:
                                res += [bk + pth[::-1] for bk in back[w]]
                        hold[w].append(pth + [w])
            if res:
                return res
            front = hold
            fwords -= toDel
        return []

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
    flds = temp.replace(", ", ",").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    beginWord = flds[0]
    endWord   = flds[1]
    wordList = flds[2].split(",")

    print("beginWord = {0}".format(beginWord))
    print("endWord   = {0}".format(endWord))
    print("wordList  = {0}".format(wordList))

    sl = Solution()
    time0 = time.time()

    result = sl.findLadders(beginWord, endWord, wordList)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

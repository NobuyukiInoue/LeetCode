import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # 132ms
        if not words:
            return 0
        if len(words) == 1:
            return 1
        words = sorted(words,key=lambda elem:len(elem))
        ref = {word:1 for word in words}
        for word in words:
            for index in range(len(word)):
                newWord = word[:index] + word[index+1:]
                if newWord in ref:
                    ref[word] = max(ref[word],ref[newWord] + 1)
            if word not in ref:
                ref[word] = 1
        ls = sorted(ref.items(),key=lambda elem:elem[1],reverse=True)
        return ls[0][1]

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
    words = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    print("words = {0}".format(words))

    sl = Solution()
    time0 = time.time()

    result = sl.longestStrChain(words)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

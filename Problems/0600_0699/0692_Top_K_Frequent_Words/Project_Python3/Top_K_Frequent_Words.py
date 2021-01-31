import collections
import heapq
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 56ms
        return [w for w, v in sorted(collections.Counter(words).items(), key = lambda x: (-x[1], x[0])) [:k]]

    def topKFrequent2(self, words: List[str], k: int) -> List[str]:
        # 56ms
        counts = collections.Counter(words)   
        freqs = sorted((-count, word) for word, count in counts.items())
        return [f[1] for f in freqs[:k]]

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
    words = flds[0].split(",")
    k = int(flds[1])

    print("words = {0}, k = {1:d}".format(words, k))

    sl = Solution()

    time0 = time.time()

    result = sl.topKFrequent(words, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

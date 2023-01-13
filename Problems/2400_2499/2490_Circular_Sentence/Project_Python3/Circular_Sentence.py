import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # 31ms
        words = sentence.split(" ")
        if len(words) == 1:
            return words[0][0] == words[0][-1]
        for i in range(len(words) - 1):
            if words[i][0] != words[i - 1][-1] or words[i][-1] != words[i + 1][0]:
                return False
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
    sentence = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    print("sentence = {0}".format(sentence))

    sl = Solution()
    time0 = time.time()

    result = sl.isCircularSentence(sentence)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        # 54ms - 67ms
        st, count, ans = [], 0, []
        for word in words:
            if word == "prev":
                count += 1
                if count <= len(st):
                    ans.append(st[-count])
                else:
                    ans.append(-1)
            else:
                st.append(int(word))
                count = 0
        return ans

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
    words = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip().split(",")
    print("words = {0}".format(words))

    sl = Solution()
    time0 = time.time()

    result = sl.lastVisitedIntegers(words)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

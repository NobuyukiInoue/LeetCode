import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # 36ms
        first_sight = {}
        stack = []
        for i, ch in enumerate(S):
            first_sight.setdefault(ch, i)
            sub_start = i
            while sub_start > first_sight[ch]:
                sub_start = stack.pop() 
            stack.append(sub_start)
        
        stack.append(len(S))
        return [stack[i + 1] - stack[i] for i in range(len(stack) - 1)]

    def partitionLabels2(self, S: str) -> List[int]:
         # 148ms
         sizes = []
         while S:
             i = 1
             while set(S[:i]) & set(S[i:]):
                 i += 1
             sizes.append(i)
             S = S[i:]
         return sizes

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
    S = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("S = {0}".format(S))

    sl = Solution()
    time0 = time.time()

    result = sl.partitionLabels(S)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

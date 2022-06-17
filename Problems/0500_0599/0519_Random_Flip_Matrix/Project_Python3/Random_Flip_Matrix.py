import bisect
import os
import sys
import time
import random
from typing import List, Dict, Tuple

class Solution:
    # 61ms - 88ms
    def __init__(self, m: int, n: int):
        self.rows, self.cols = m, n
        self.limit = m*n
        self.used = set()

    def flip(self) -> List[int]:
        val =  random.randint(0, self.limit - 1)
        while val in self.used:
            val += 1
            if val == self.limit:
                val = 0
        self.used.add(val)
        return list(divmod(val, self.cols))

    def reset(self) -> None:
        self.used = set()

    """
    # 83ms -133ms
    def __init__(self, m: int, n: int):
        self.mn = m * n
        self.n_cols = n
        self.reset()

    def flip(self) -> List[int]:
        index = int(random.random() * (self.mn - len(self.removed)))
        alreadySkipped = 0
        while True:
            removedBefore = bisect.bisect(self.removed, index)
            if removedBefore == alreadySkipped:
                break
            index += removedBefore - alreadySkipped
            alreadySkipped = removedBefore
        bisect.insort(self.removed, index)
        return (index // self.n_cols, index % self.n_cols)

    def reset(self) -> None:
        self.removed = []
    """

    """
    # Time Limit Exceeded.
    def __init__(self, m: int, n: int):
        self.matrix = [[0, 0] for i in range(m) for j in range(n)]
        self.m, self.n = m, n
        self.candidate = [[i, j] for i in range(m) for j in range(n)]

    def flip(self) -> List[int]:
        idx = int(random.random()*len(self.candidate))
        res = self.candidate[idx]
        self.candidate = self.candidate[:idx] + self.candidate[idx + 1:]
        return res

    def reset(self) -> None:
        self.__init__(self.m, self.n)
    """

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()

    def main(self, cmds, args):
        res = []
        randomFlipMatrix = False
        for i in range(len(cmds)):
            if cmds[i] == "Solution":
                randomFlipMatrix = True
                res.append(None)
                print("Exec Solution({0:d}, {1:d}).".format(args[i][0], args[i][1]))
            else:
                if randomFlipMatrix is False:
                    print("randomFlipMatrix not found... {0}".format(cmds[i]))
                    exit(1)
                elif cmds[i] == "flip":
                    res.append(self.flip())
                    print("flip() ... {0}".format(res[-1]))
                elif cmds[i] == "reset":
                    self.reset()
                    res.append(None)
                    print("reset() .... {0}".format(res[-1]))
                else:
                    print("error... {0}".format(cmds[i]))
                    exit(1)
        return res

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
    flds = temp.replace("\"","").replace(", ",",").rstrip().split("],[[")
    cmds = flds[0].replace("[", "").replace("]", "").split(",")
    args = flds[1].replace("]]]","").split("],[")
    for i in range(len(args)):
        args[i] = [int(_) for _ in args[i].split(",") if args[i] != ""]

    print("cmds[] = {0}".format(cmds))
    print("args[] = {0}".format(args))

    sl = Solution(args[0][0], args[0][1])
    time0 = time.time()
    result = sl.main(cmds, args)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

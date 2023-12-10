import random
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution2:
    # 137ms - 141ms

    def __init__(self, nums: List[int]):
        self.arr = nums[:]

    def reset(self) -> List[int]:
        return self.arr

    def shuffle(self) -> List[int]:
        ans = self.arr[:]
        for i in range(len(ans)):
            swp_num = random.randrange(i, len(ans))
            ans[i], ans[swp_num] = ans[swp_num], ans[i]
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

class Solution:
    def main(self, cmds, args):
        res = []
        for i, cmd in enumerate(cmds):
            if cmd == "Solution":
                sol = Solution2(args[0])
                res.append(args[0])
                print("Solution() ... {0}".format(args[0]))
            else:
                if sol is None:
                    print("Solution not found... {0}".format(cmds[i]))
                    exit(1)
                elif cmds[i] == "reset":
                    res.append(sol.reset())
                    print("reset() ... {0}".format(res[-1]))
                elif cmds[i] == "shuffle":
                    res.append(sol.shuffle())
                    print("shuffle() ... {0}".format(res[-1]))
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
    flds = temp.replace("\"", "").replace(", ", ",").rstrip().split("],[[")
    cmds = flds[0].replace("[", "").split(",")
    args = flds[1].replace("]]]", "").split("],[")
    for i, arg in enumerate(args):
        if arg != "":
            args[i] = [int(_) for _ in arg.replace("[", "").replace("]", "").split(",")]
        else:
            args[i] = []

    print("cmds[] = {0}".format(cmds))
    print("args[] = {0}".format(args))

    sl = Solution()
    time0 = time.time()
    result = sl.main(cmds, args)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

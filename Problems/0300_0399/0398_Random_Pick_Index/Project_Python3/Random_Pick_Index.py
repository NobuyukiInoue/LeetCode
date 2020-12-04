import os
import sys
import time

import random

#class Solution:
class RandomPickIndex:
    # 272ms

#   def __init__(self, nums: List[int]):
    def __init__(self, nums: [int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        return random.choice([k for k, v in enumerate(self.nums) if v == target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

class Solution:
    def main(self, cmds, args):
        res = []
        for i in range(len(cmds)):
            if cmds[i] == "Solution":
                randomPickIndex = RandomPickIndex(args[i])
                res.append(None)
                print("Exec RandomPickIndex().")
            else:
                if randomPickIndex is None:
                    print("randomPickIndex not found... {0}".format(cmds[i]))
                    exit(1)
                elif cmds[i] == "pick":
                    res.append(randomPickIndex.pick(args[i][0]))
                    print("pick({0}) ... {1}".format(args[i][0], res[-1]))
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
        args[i] = [int(_) for _ in args[i].replace("[", "").replace("]", "").split(",")]

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

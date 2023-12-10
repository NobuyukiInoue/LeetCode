import random
import os
import sys
import time
from typing import List, Dict, Tuple

class RandomizedSet:
    # 305ms - 321ms

    def __init__(self):
        self.data_map = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        self.data_map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not val in self.data_map:
            return False
        last_elem_in_list = self.data[-1]
        index_of_elem_to_remove = self.data_map[val]
        self.data_map[last_elem_in_list] = index_of_elem_to_remove
        self.data[index_of_elem_to_remove] = last_elem_in_list
        self.data[-1] = val
        self.data.pop()
        self.data_map.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)

class RandomizedSet2:
    # 584ms - 586ms

    def __init__(self):
        self.arr = []

    def insert(self, val: int) -> bool:
        if not val in self.arr:
            self.arr.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.arr:
            self.arr.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return self.arr[random.randrange(0, len(self.arr))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

class Solution:
    def main(self, cmds, args):
        res = []
        for i, cmd in enumerate(cmds):
            if cmd == "RandomizedSet":
                randmizeset = RandomizedSet()
                res.append(None)
                print("RandomizedSet() ... {0}".format(args[0]))
            else:
                if randmizeset is None:
                    print("RandomizedSet not found ... {0}".format(cmds[i]))
                    exit(1)
                elif cmds[i] == "insert":
                    res.append(randmizeset.insert(args[i][0]))
                    print("insert({0:d}) ... {1}".format(args[i][0], res[-1]))
                elif cmds[i] == "remove":
                    res.append(randmizeset.remove(args[i][0]))
                    print("remove({0:d}) ... {1}".format(args[i][0], res[-1]))
                elif cmds[i] == "getRandom":
                    res.append(randmizeset.getRandom())
                    print("getrandom() ... {0:d}".format(res[-1]))
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
            args[i] = [int(args[i])]
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

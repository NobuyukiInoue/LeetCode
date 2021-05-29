import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class LRUCache:
    # 160ms
    def __init__(self, capacity: int):
        self.od, self.cap = collections.OrderedDict(), capacity

    def get(self, key: int) -> int:
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            del self.od[key]
        elif len(self.od) == self.cap:
            self.od.popitem(False)
        self.od[key] = value        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class Solution:
    def main(self, cmds, args):
        res = []
        for i in range(len(cmds)):
            if cmds[i] == "LRUCache":
                lrucache = LRUCache(args[i][0])
                res.append(None)
                print("Exec LRUCache().")
            else:
                if lrucache is None:
                    print("LRUCache not found... {0}".format(cmds[i]))
                    exit(1)
                elif cmds[i] == "get":
                    res.append(lrucache.get(args[i][0]))
                    print("get({0}) ... {1}".format(args[i], res[-1]))
                elif cmds[i] == "put":
                    res.append(lrucache.put(args[i][0], args[i][1]))
                    print("put({0}) ... {1}".format(args[i], res[-1]))
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
        args[i] = [int(_) for _ in args[i].split(",")]

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

import os
import sys
import time

class OrderedStream:
    # 220ms
    def __init__(self, n: int):
        self.data = [None]*(n + 1)
        self.ptr = 0

    def insert(self, id: int, value: str) -> List[str]:
        self.data[id - 1] = value
        while self.data[self.ptr]:
            yield self.data[self.ptr]
            self.ptr += 1

class OrderedStream2:
    # 224ms
    def __init__(self, n: int):
        self.stream = [None]*n
        self.currentIndex = 0

#   def insert(self, id: int, value: str) -> List[str]:
    def insert(self, id: int, value: str) -> [str]:
        self.stream[id - 1] = [id, value]
        res = []
        for i in range(self.currentIndex, len(self.stream)):
            if self.stream[i] is None:
                break
            res.append(self.stream[i][1])
        self.currentIndex = i
        return res

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)


class Solution:
    def main(self, cmds, args):
        res = []
        for i in range(len(cmds)):
            if cmds[i] == "OrderedStream":
                orderedStream = OrderedStream(int(args[i][0]))
                res.append(None)
                print("Exec OrderedStream().")
            else:
                if orderedStream is None:
                    print("OrderedStream not found... {0}".format(cmds[i]))
                    exit(1)
                elif cmds[i] == "insert":
                    res.append(orderedStream.insert(int(args[i][0]), args[i][1]))
                    print("insert({0}) ... {1}".format(args[i], res[-1]))
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
        args[i] = args[i].split(",")

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

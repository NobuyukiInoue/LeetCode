# coding: utf-8

import os
import sys
import time
import collections

class RecentCounter:
    def __init__(self):
        self.p = collections.deque()

    def ping(self, t: int) -> int:
        self.p.append(t)
        while self.p[0] < t - 3000:
            self.p.popleft()
        return len(self.p)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

class Cmds:
    def __init__(self, cmd, arg):
        self.cmd = cmd
        self.arg = arg

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
    flds = temp.rstrip().split("],[[")
    flds1 = flds[0].replace("[", "").replace("]", "").replace("\"", "").split(",")
    flds2 = flds[1].replace("[", "").replace("]", "").replace("\"", "").split(",")

    if len(flds1) != len(flds2):
        print("cmds count is not equal args count.")
        exit(1)

    exec_list = []*len(flds1)

    for i in range(len(flds1)):
        print("cmd[{0:d}] = {1}({2})".format(i, flds1[i], flds2[i]))
        if flds2[i] == '':
            exec_list.append(Cmds(flds1[i], flds2[i]))
        else:
            exec_list.append(Cmds(flds1[i], int(flds2[i])))
    
    print()
    time0 = time.time()

    result = [""]*len(exec_list)
    for i in range(len(exec_list)):
        if exec_list[i].cmd == "RecentCounter":
            rc = RecentCounter()
            result[i] = None
            print("Execute ... {0}()".format(exec_list[i].cmd))
        elif exec_list[i].cmd == "ping":
            result[i] = rc.ping(exec_list[i].arg)
            print("Execute ... {0}({1})".format(exec_list[i].cmd, exec_list[i].arg))
        else:
            print("{0} is not found.".format(exec_list[i].cmd))
            exit(1)

    time1 = time.time()

    print("\nresult = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

import os
import sys
import time

import bisect

class MyCalendar(object):
    # 180ms

    def __init__(self):
        self.intervals = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if end <= start:
            return False

        i = bisect.bisect_right(self.intervals, start)
        if i % 2:            # start is in some stored interval
            return False

        j = bisect.bisect_left(self.intervals, end)
        if i != j:
            return False

        self.intervals[i:i] = [start, end]

        return True

class MyCalendar2:
    # 752ms
    def __init__(self):
        self.books = []

    def book(self, start: int, end: int) -> bool:
        if len(self.books) == 0:
            self.books.append([start, end])
            return True
        for book in self.books:
            if book[0] < end and start < book[1]:
                return False

        self.books.append([start, end])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


class Solution:
    def main(self, cmds, args):
        res = []
        for i in range(len(cmds)):
            if cmds[i] == "MyCalendar":
                mycalendar = MyCalendar()
                res.append(None)
                print("Exec MyCalendar().")
            else:
                if mycalendar is None:
                    print("mycalendar not found... {0}".format(cmds[i]))
                    exit(1)
                elif cmds[i] == "book":
                    res.append(mycalendar.book(args[i][0], args[i][1]))
                    print("book({0}, {1}) ... {2}".format(args[i][0], args[i][1], res[-1]))
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
    flds1 = flds[1].replace("]]]","").split("],[")
    print(flds1)
    args = [None]*len(flds1)
    for i in range(len(args)):
        if len(flds1[i]) == 0:
            args[i] = []
        else:
            args[i] = [int(n) for n in flds1[i].split(",")]

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

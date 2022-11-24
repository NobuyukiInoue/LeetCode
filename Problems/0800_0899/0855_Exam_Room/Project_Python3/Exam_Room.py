import bisect
import os
import sys
import time
from typing import List, Dict, Tuple

from heapq import heappush, heappop

class ExamRoom:
    # 142ms - 252ms
    def __init__(self, n: int):
        self.N = n
        self.heap = []
        self.avail_first = {}
        self.avail_last = {}
        self.put_segment(0, self.N - 1)

    def put_segment(self, first: int, last: int) -> None:
        if first == 0 or last == self.N - 1:
            priority = last - first
        else:
            priority = (last - first) // 2
        segment = [-priority, first, last, True]
        self.avail_first[first] = segment
        self.avail_last[last] = segment
        heappush(self.heap, segment)

    def seat(self) -> int:
        while True:
            _, first, last, is_valid = heappop(self.heap)
            if is_valid:
                del self.avail_first[first]
                del self.avail_last[last]
                break
        if first == 0:
            ret = 0
            if first != last:
                self.put_segment(first + 1, last)
        elif last == self.N - 1:
            ret = last
            if first != last:
                self.put_segment(first, last - 1)
        else:
            ret = first + (last - first) // 2
            if ret > first:
                self.put_segment(first, ret - 1)
            if ret < last:
                self.put_segment(ret + 1, last)
        return ret

    def leave(self, p: int) -> None:
        first, last = p, p
        left, right = p - 1, p + 1
        if left >= 0 and left in self.avail_last:
            segment_left = self.avail_last.pop(left)
            segment_left[3] = False
            first = segment_left[1]
        if right < self.N and right in self.avail_first:
            segment_right = self.avail_first.pop(right)
            segment_right[3] = False
            last = segment_right[2]
        self.put_segment(first, last)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)

"""
class ExamRoom2:
    # 287ms - 332ms
    MAX_L = -100011100011
    MAX_R = 100011100011

    def __init__(self, n: int):
        self.N = n
        self.h = []
        self.lr_map = {}
        self.seating = set()
        
        heappush(self.h, (-min(-ExamRoom.MAX_L, ExamRoom.MAX_R), 0))
        self.lr_map[0] = (ExamRoom.MAX_L, ExamRoom.MAX_R)
        
    def _add_candidate(self, l, r):
        mid = (l + r) // 2
        mid = max(mid, 0)
        mid = min(mid, self.N - 1)
        if l < mid < r:
            self.lr_map[mid] = (l, r)
            heappush(self.h, (-min(mid - l, r - mid), mid))        

    def seat(self) -> int:
        dist, seat, l, r = None, None, None, None
        while seat is None or seat in self.seating or -dist != min(seat - l, r - seat):
            dist, seat = heappop(self.h)
            l, r = self.lr_map[seat]
        self._add_candidate(l, seat)            
        self._add_candidate(seat, r)
        if l >= 0:
            self.lr_map[l] = self.lr_map[l][0], seat
        if r <= self.N-1:
            self.lr_map[r] = seat, self.lr_map[r][1]
        self.seating.add(seat)
        return seat

    def leave(self, p: int) -> None:
        l, r = self.lr_map[p]
        if l >= 0:
            self.lr_map[l] = (self.lr_map[l][0], r)
        if r <= self.N-1:
            self.lr_map[r] = (l, self.lr_map[r][1])
        self._add_candidate(l, r)
        self.seating.remove(p)

class ExamRoom3:
    # 4321ms - 4430ms
    def __init__(self, n: int):
        self.N, self.L = n, []

    def seat(self) -> int:
        N, L = self.N, self.L
        if not L: res = 0
        else:
            d, res = L[0], 0
            for a, b in zip(L, L[1:]):
                if (b - a) // 2 > d:
                    d, res = (b - a) // 2, (b + a) // 2
            if N - 1 - L[-1] > d:
                res = N - 1
        bisect.insort(L, res)
        return res

    def leave(self, p: int) -> None:
        self.L.remove(p)
"""

class Solution:
    def execExamRoom(self, cmds : List[str], args: List[str]) -> List[int]:
        res = []
        for i in range(len(cmds)):
            if cmds[i] == "ExamRoom":
                n = int(args[i])
                examRoom = ExamRoom(n)
                print("Execute ExamRoom()")
                res.append(n)
            else:
                if examRoom is None:
                    print("examRoom not found... {0}".format(cmds[i]))
                    exit(1)
                elif cmds[i] == "seat":
                    result = examRoom.seat()
                    print("seat()  ... {0:d}".format(result))
                    res.append(result)
                elif cmds[i] == "leave":
                    examRoom.leave(int(args[i]))
                    print("leave() ... null")
                    res.append(None)
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
    flds = temp.replace(" ","").replace("\"","").rstrip().split("],[[")
    cmds = flds[0].replace("[[","").split(",")
    args = [_ for _ in flds[1].replace("]]]", "").split("],[")]

    print("cmds[] = {0}",format(cmds))
    print("args[] = {0}".format(args))

    sl = Solution()
    time0 = time.time()

    result = sl.execExamRoom(cmds, args)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

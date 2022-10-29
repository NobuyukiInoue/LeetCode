# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        # 299ms - 760ms
        prev, ans = 0, (0, 0)
        for id, curr in logs:
            ans = min(ans,(prev - curr, id))
            prev = curr
        return ans[1]

    def hardestWorker2(self, n: int, logs: List[List[int]]) -> int:
        # 309ms - 828ms
        best_id = best_time = start = 0
        for emp_id, end in logs:
            time = end - start
            if time > best_time or (time == best_time and best_id > emp_id):
                best_id = emp_id
                best_time = time
            start = end
        return best_id

    def hardestWorker3(self, n: int, logs: List[List[int]]) -> int:
        # 319ms - 840ms
        id = logs[0][0]
        last_end_time = max_work_time = logs[0][1]
        for i in range(1, len(logs)):
            work_time = logs[i][1] - last_end_time
            if work_time == max_work_time:
                id = min(logs[i][0], id)
            elif work_time > max_work_time:
                max_work_time = work_time
                id = logs[i][0]
            last_end_time = logs[i][1]
        return id

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
    flds = temp.replace(" ","").replace("\"","").replace("]]]","").rstrip().split("],[[")

    n = int(flds[0].replace("[[",""))
    logs = [[int(col) for col in data.split(",")] for data in flds[1].split("],[")]
    print("nums = {0}, logs = {1}".format(n, logs))

    sl = Solution()
    time0 = time.time()

    result = sl.hardestWorker(n, logs)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

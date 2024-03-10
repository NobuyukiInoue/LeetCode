import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 343ms - 353ms
        people.sort()
        ans, i, j = 0, 0, len(people) - 1
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    
    people, limit = [int(num) for num in flds[0].split(",")], int(flds[1])
    print("people = {0}, limit = {1:d}".format(people, limit))

    sl = Solution()
    time0 = time.time()

    result = sl.numRescueBoats(people, limit)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

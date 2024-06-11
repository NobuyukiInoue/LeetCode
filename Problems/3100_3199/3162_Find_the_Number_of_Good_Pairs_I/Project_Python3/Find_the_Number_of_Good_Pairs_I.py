import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # 47ms - 49ms
        ans = 0
        for num1 in nums1:
            for num2 in nums2:
                if num1%(num2*k) == 0:
                    ans += 1
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
    
    nums1 = [int(num) for num in flds[0].split(",")]
    nums2 = [int(num) for num in flds[1].split(",")]
    k = int(flds[2])
    print("nums1 = {0}, nums2 = {1}, k = {2:d}".format(nums1, nums2, k))

    sl = Solution()
    time0 = time.time()

    result = sl.numberOfPairs(nums1, nums2, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

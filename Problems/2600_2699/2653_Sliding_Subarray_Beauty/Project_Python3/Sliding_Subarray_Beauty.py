import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        # 4528ms - 4576ms 
        n, freq, j = len(nums), [0]*51, 0
        ans = []
        for i in range(n):
            if nums[i] < 0:
                freq[abs(nums[i])] += 1
            if i - j + 1 >= k:
                cnt = 0
                for L in range(50, 0, -1):
                    cnt += freq[L]
                    if cnt >= x:
                        ans.append(-L)
                        break
                if cnt < x:
                    ans.append(0)
                if nums[j] < 0:
                    freq[abs(nums[j])] -= 1
                j += 1
        return ans
        
    def getSubarrayBeauty_bad1(self, nums: List[int], k: int, x: int) -> List[int]:
        # Time Limit Exceeded.
        res = []
        for i in range(0, len(nums) - k + 1):
            temp = nums[i:i+k]
            temp.sort()
            if temp[x - 1] < 0:
                res.append(temp[x - 1])
            else:
                res.append(0)
        return res

    def getSubarrayBeauty_bad2(self, nums: List[int], k: int, x: int) -> List[int]:
        # Time Limit Exceeded.
        res = []
        for i in range(0, len(nums) - k + 1):
            temp = []
            for j in range(i, i + k):
                if nums[j] < 0:
                    temp.append(nums[j])
            if x - 1 < 0 or x - 1 >= len(temp) or len(temp) == 0:
                res.append(0)
            else:
                temp.sort()
                if temp[x - 1] < 0:
                    res.append(temp[x - 1])
                else:
                    res.append(0)
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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    nums = [int(n) for n in flds[0].split(",")]
    k, x = int(flds[1]), int(flds[2])
    print("nums = {0}, k = {1:d}, x = {2:d}".format(nums, k, x))

    sl = Solution()
    time0 = time.time()

    result = sl.getSubarrayBeauty(nums, k, x)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

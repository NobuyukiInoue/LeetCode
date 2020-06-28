# coding: utf-8

import os
import sys
import time

class Solution:
#   def triangleNumber(self, nums: List[int]) -> int:
    def triangleNumber2(self, nums):
        # 260ms
        nums.sort()
        count, nums_length = 0, len(nums)
        for i in range(nums_length - 1, 1, -1):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    count += r - l
                    r -= 1
                else:
                    l += 1
        return count

    def triangleNumber(self, nums):
        # 76ms
        nums_max = max(nums)
        if nums_max == 0:
            return 0
        count = [0] * (nums_max + 1)
        N = 0
        for x in nums:
            if x:
                count[x] += 1
                N += 1
        keys = [x for x in range(nums_max + 1) if count[x]]
        
        psum = [0]
        for c in count:
            psum.append(psum[-1] + c)

        ans = 0
        for i1, k1 in enumerate(keys):
            for i2 in range(i1, len(keys)):
                k2 = keys[i2]
                if i1 != i2:
                    multiplicity = count[k1] * count[k2]
                else:
                    multiplicity = count[k1] * (count[k1] - 1) // 2
                
                if k1 + k2 <= nums_max:
                    ans += multiplicity * psum[k1 + k2]
                else:
                    multiplicity += count[k1] * (psum[-1] - psum[k2+1])
                    ans += multiplicity * N
                    break
        
        return ans - N*(N*N - 1)//3


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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()
    time0 = time.time()
    result = sl.triangleNumber(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

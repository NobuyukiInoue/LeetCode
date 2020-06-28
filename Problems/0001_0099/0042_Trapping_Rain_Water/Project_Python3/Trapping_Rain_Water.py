# coding: utf-8

import os
import sys
import time

class Solution:
#   def trap(self, height: List[int]) -> int:
    def trap(self, height):
        # 56ms - 72ms
        i, j = 0, len(height) - 1
        left_max = right_max = 0
        ans = 0
        while i < j:
            left_max = max(left_max, height[i])
            right_max = max(right_max, height[j])
            if left_max <= right_max:
                ans += left_max - height[i]
                i += 1
            else:
                ans += right_max - height[j]
                j -= 1
        return ans

    def trap_work(self, height):
        outputs = 0
        for i in range(len(height) - 1):
            if height[i + 1] >= height[i]:
                continue
            for target_h in range(height[i], 0, -1):
                if height[i + 1] == target_h:
                    break
                for j in range(i + 2, len(height)):
                    if target_h <= height[j]:
                        outputs += j - i - 1
                        break
        return outputs

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")
    height = [int(n) for n in flds]

    sl = Solution()
    time0 = time.time()

    result = sl.trap(height)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

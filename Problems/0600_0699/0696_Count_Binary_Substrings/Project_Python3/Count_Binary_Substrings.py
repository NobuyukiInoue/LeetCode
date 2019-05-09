# coding: utf-8

import os
import sys
import time

class Solution:
#    def countBinarySubstrings(self, s: str) -> int:
    def countBinarySubstrings(self, s):
        t = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split()))
        return sum(min(a, b) for a, b in zip(t, t[1:]))

    def countBinarySubstrings_work(self, s):
        if len(s) <= 1:
            return 0
        result = 0
        for i in range(len(s)):
            target_src = s[i]
            for j in range(i + 1, len(s)):
                if s[j] != target_src:
                    break
            count1 = j - i
            if target_src == "0":
                target_nxt = "1"
            else:
                target_nxt = "0"
            flg = True
            for k in range(j, len(s)):
                count2 = k - j
                if s[k] != target_nxt:
                    flg = False
                    break
                if count2 == count1:
                    flg = False
                    break
            if flg:
                k = len(s)
                count2 = k - j
            if count1 == count2 and i != k:
                '''
                if k < j:
                    print("s[%d:] = %s" %(i, s[i:]))
                else:
                    print("s[%d:%d] = %s" %(i, k, s[i:k]))
                '''
                result += 1
        return result

def str_to_int_array(flds):
    if len(flds) <= 0:
        return None
    temp = flds.split(",")
    nums = [0]*len(temp)
    for i in range(len(temp)):
        nums[i] = int(temp[i])
    return nums

def main():
    argv = sys.argv
    argc = len(argv)

    if (argc < 2):
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    s = temp.replace("\"","").replace(" ","").replace("[","").replace("]","").rstrip()
    print("s = %s\n" %s)

    time0 = time.time()

    sl = Solution()
    result = sl.countBinarySubstrings(s)

    time1 = time.time()
    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()

# coding: utf-8

import itertools
import os
import sys
import time


class Solution:
    def readBinaryWatch(self, num):
        ref = [1,2,4,8,16,32,64,128,256,512]
        st = set()
        for x in itertools.combinations(ref, num):
            top = sum(i for i in x if i <= 8)
            bottom = sum(i//16 for i in x if i >= 16)
            if top < 12 and bottom < 60:
                st.add((top, bottom))
        
        result = []
        for hour, minute in st:
            result.append(str(hour) + ':' + str(minute).rjust(2, '0'))
        return sorted(result)

    def readBinaryWatch2(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for i in range(0, num + 1):
            j = num - i
            if i >= 4 or j >= 6:
                continue
            hour = self.helper(4, i)
            min = self.helper(6, j)
            hour = self.shape(hour, isHour=True)
            min = self.shape(min, isMin=True)
            for m in hour:
                for n in min:
                    if len(str(n)) != 1:
                        res.append(str(m) + ":" + str(n))
                    else:
                        res.append(str(m) + ":0" + str(n))
        return res

    def shape(self, arr, isHour=False, isMin=False):
        if isHour:
            a = [i for i in arr if i < 12]
        if isMin:
            a = [i for i in arr if i < 60]
        return a

    def helper(self, n, m):
        res = []
        self.backtracking(n, m, 0, 0, res)
        # if len(res) == 0:
        #     res.append(0)
        return res

    def backtracking(self, n, m, pos, sum, res):
        if (m == 0):
            res.append(sum)
            return
        if (pos == n):
            return
        for i in range(pos, n):
            self.backtracking(n, m - 1, pos + 1, sum + 2 ** (n - pos - 1), res)
            self.backtracking(n, m, pos + 1, sum, res)
            return

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
        print("argv[1] = %s" %temp)
        loop_main(temp)


def loop_main(temp):
    num = int(temp)

    time0 = time.time()

    sl = Solution()
    result = sl.readBinaryWatch(num)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
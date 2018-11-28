# coding: utf-8

import sys
import time

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1,i):
                result[i][j] = result[i-1][j-1] + result[i-1][j]
        return result

    def generate_old(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[]]*numRows
        for i in range(numRows):
            result[i] = [1]*(i + 1)
        #   result[i][0] = 1
        #   result[i][i] = 1
            for j in range(1, i):
                result[i][j] = result[i - 1][j] + result[i - 1][j - 1]
        return result


def test_main(numRows):
    sl = Solution()
    result = sl.generate(numRows)
    print("result = %s" %result)


def main():
    args = sys.argv
    argc = len(args)

    print("args[0] = %s %s" %(args[0], args[1]) )
    time0 = time.time()

    test_main(int(args[1]))

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()

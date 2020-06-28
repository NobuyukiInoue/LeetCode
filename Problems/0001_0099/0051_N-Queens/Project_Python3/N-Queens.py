# coding: utf-8

import copy
import os
import sys
import time
import itertools

class Solution:
#   def solveNQueens(self, n: int) -> List[List[str]]:
    def solveNQueens(self, n):
        # 48ms
        res = []
        def dfs(i, l, r, m, arr):
            if i == n:
                res.append(arr)
            else:
                l = l[1:] + [0]
                r = [0] + r[:-1]
                for j in range(n):
                    if m[j] == l[j] == r[j] == 0:
                        l[j] = r[j] = m[j] = 1 
                        dfs(i + 1, l, r, m, arr + [("." * j) + "Q" + ("." * (n - j - 1))])
                        l[j] = r[j] = m[j] = 0
        dfs(0, [0] * n, [0] * n, [0] * n, [])
        return res

    def solveNQueens2(self, n):
        # 120ms
        res = []
        self.dfs([-1]*n, 0, [], res)
        return res
    
    def dfs(self, nums, index, path, res):
        if index == len(nums):
            res.append(path)
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):
                tmp = "."*len(nums)
                self.dfs(nums, index + 1, path + [tmp[:i] + "Q" + tmp[i+1:]], res)

    def valid(self, nums, n):
        for i in range(n):
            if abs(nums[i] - nums[n]) == n - i or nums[i] == nums[n]:
                return False
        return True

    def solveNQueens2(self, n):
        # 624ms
        return [['.' * v + 'Q' + '.' * (n - v - 1) for v in c] for c in itertools.permutations(range(n))
                if (len(set(i + v for i, v in enumerate(c))) == n) and
                (len(set(i - v for i, v in enumerate(c))) == n)]


    """
    def solveNQueens_bad(self, n):
        table = [['.' for j in range(n)] for i in range(n)]
        res_temp = []
        def helper(n, table):
            len_row, len_col = len(table), len(table[0])
            for i in range(len_row):
                for j in range(len_col):
                    if table[i][j] == ".":
                        if n - 1 == 0:
                            table[i][j] = "Q"
                            if table not in res_temp:
                                res_temp.append(table)
                                return
                        else:
                            temp_table = copy.deepcopy(table)
                            self.putQueen(temp_table, i, j)
                            helper(n - 1, temp_table)
            return
        helper(n, table)

        results = [["" for row in range(len(res_temp[index]))] for index in range(len(res_temp))]
        for index in range(len(res_temp)):
            for row in range(len(res_temp[index])):
                fld = ""
                for col in range(len(res_temp[index][row])):
                    if res_temp[index][row][col] == "x":
                        fld += "."
                    else:
                        fld += res_temp[index][row][col]
                results[index][row] = fld

        return results

    def enablePutQueen(self, table, i, j):
        if table[i][j] == "Q" or table[i][j] == "x":
            return False
        len_row, len_col = len(table), len(table[0])
        for row in range(len_row):
            if table[row][j] == "Q" or table[row][j] == "x":
                return False
        for col in range(len_col):
            if table[i][col] == "Q" or table[i][col] == "x":
                return False
        for k in range(len_row):
            if i - k >= 0 and j - k >= 0:
                if table[i-k][j-k] == "Q" or table[i-k][j-k] == "x":
                    return False
            if i - k >= 0 and j + k < len_col:
                if table[i-k][j+k] == "Q" or table[i-k][j+k] == "x":
                    return False
            if i + k < len_row and j - k >= 0:
                if table[i+k][j-k] == "Q" or table[i+k][j-k] == "x":
                    return False
            if i + k < len_row and j + k < len_col:
                if table[i+k][j+k] == "Q" or table[i+k][j+k] == "x":
                    return False
        return True

    def putQueen(self, table, i, j):
        len_row, len_col = len(table), len(table[0])
        for row in range(len_row):
            table[row][j] = "x"
        for col in range(len_col):
            table[i][col] = "x"
        for k in range(len_row):
            if i - k >= 0 and j - k >= 0:
                table[i-k][j-k] = "x"
            if i - k >= 0 and j + k < len_row:
                table[i-k][j+k] = "x"
            if i + k < len_row and j - k >= 0:
                table[i+k][j-k] = "x"
            if i + k < len_row and j + k < len_col:
                table[i+k][j+k] = "x"
        table[i][j] = "Q"
    """

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

    n = int(flds)
    print("n = {0}".format(n))

    sl = Solution()
    time0 = time.time()

    result = sl.solveNQueens(n)

    time1 = time.time()

    for i in range(len(result)):
        print_result(i, result[i])

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

def print_result(num, result):
    print("result[{0}] = \n[".format(num))
    for i in range(len(result)):
        if i == 0:
            print(" {0}".format(result[i]))
        else:
            print(",{0}".format(result[i]))
    print("]")

if __name__ == "__main__":
    main()

# coding: utf-8

import copy
import os
import sys
import time

class Solution:
#   def addOperators(self, num: str, target: int) -> List[str]:
    def addOperators(self, num, target):
        # 292ms
        if not num:
            return []
        res = []

        def helper(start, expr, val, prev):
            if val == target and start == len(num):
                res.append(expr)
                return
            if start < len(num) and max(1, abs(prev))*(int(num[start:])) < abs(target - val):
                return
            for i in range(start, len(num)):
                curr = num[start: i+1]
                if len(curr) != len(str(int(curr))):
                    break
                if start == 0:
                    helper(i + 1, curr, int(curr), int(curr))
                else:
                    helper(i + 1, expr + '+' + curr, val + int(curr), int(curr))
                    helper(i + 1, expr + '-' + curr, val - int(curr), -int(curr))
                    helper(i + 1, expr + '*' + curr, val - prev+prev*int(curr), prev*int(curr))
        
        helper(0, '', 0, 0)
        return res


    def addOperators2(self, num, target):
        # 588ms
        if not num:
            return []
        table = [(num[0], int(num[0]), int(num[0]))]
        result = []
        for i in range(1, len(num)):
            cur = int(num[i])
            temp = []
            for string, a, b in table:
                p = len(string) - 1
                while p >= 0 and ord(string[p]) - ord('0') >= 0 and ord(string[p]) - ord('0') <= 9:
                    p -= 1
                p += 1
                if i == len(num) - 1:
                    if a + cur == target:
                        result.append(string + "+" + num[i])
                    if a - cur == target:
                        result.append(string + "-" + num[i])
                    if a - b + b * cur == target:
                        result.append(string + "*" + num[i])
                    
                    if ord(string[p]) - ord('0') != 0:
                        if a - b + b*10 + (b*cur)/int(string[p:]) == target:
                            result.append(string+num[i])
                else:
                    temp.append((string + "+" + num[i], a + cur, cur))
                    temp.append((string + "-" + num[i], a - cur, -cur))
                    temp.append((string + "*" + num[i], a - b + b * cur, b*cur))
                    if ord(string[p]) - ord('0') != 0:
                        temp.append((string + num[i], a - b + b * 10 + (b*cur)/int(string[p:]), b * 10 + (b*cur)/int(string[p:])))
                table = temp
        return result

    def addOperators3(self, num, target):
        # 688ms
        res = []
        self.dfs3(0, 0, 0, num, target, "", res)
        return res

    def dfs3(self, left, right, si, num, target, expr, res):
        if si >= len(num):
            if left + right == target:
                res.append(expr)
            return
        curr = 0
        for i in range(si, len(num)):
            curr = curr*10 + ord(num[i]) - ord('0')
            currNum = num[si : i+1]
            if currNum[0] == '0' and len(currNum) > 1:
                continue
            if si == 0:
                self.search(0, curr, i + 1, num, target, currNum, res)
            else:
                self.search(left + right, curr, i + 1, num,target, expr + '+' + currNum,res)
                self.search(left + right, -curr, i + 1, num,target, expr + '-' + currNum,res)
                self.search(left, right*curr, i + 1, num, target, expr + '*' + currNum,res)

    def addOperators4(self, num, target):
        # 848ms
        res, self.target = [], target
        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != "0"):
                self.dfs4(num[i:], num[:i], int(num[:i]), int(num[:i]), res)
        return res

    def dfs4(self, num, temp, cur, last, res):
        if not num:
            if cur == self.target:
                res.append(temp)
            return
        for i in range(1, len(num)+1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != "0"):
                self.dfs3(num[i:], temp + "+" + val, cur + int(val), int(val), res)
                self.dfs3(num[i:], temp + "-" + val, cur - int(val), -int(val), res)
                self.dfs3(num[i:], temp + "*" + val, cur - last + last*int(val), last*int(val), res)

    def addOperators5(self, num, target):
        # 1124ms
        self.res, self.target = [], target
        if len(num) == 0:
            return self.res
        path = [" " for i in range(len(num)*2 - 1)]
        digits = copy.copy(num)
        n = 0
        for i in range(len(digits)):
            n = n*10 + int(digits[i])
            path[i] = digits[i]
            self.dfs5(copy.copy(path), i + 1, 0, n, digits, i + 1)
            if n == 0:
                break
        return self.res

    def dfs5(self, path, length, left, cur, digits, pos):
        if pos == len(digits):
            if left + cur == self.target:
                self.res.append(self.join(path))
            return
        n = 0
        j = length + 1
        for i in range(pos, len(digits)):
            n = n*10 + int(digits[i])
            path[j] = digits[i]
            j += 1

            path[length] = '+'
            self.dfs5(copy.copy(path), j, left + cur, n, digits, i + 1)

            path[length] = '-'
            self.dfs5(copy.copy(path), j, left + cur, -n, digits, i + 1)

            path[length] = '*'
            self.dfs5(copy.copy(path), j, left, cur * n, digits, i + 1)

            if digits[pos] == '0':
                break

    def join(self, path):
        resultStr = ""
        for ch in path:
            if ch == " ":
                continue
            resultStr += ch
        return resultStr


def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")

    num = flds[0]
    target = int(flds[1])
    print("num = {0}, target = {1:d}".format(num, target))

    time0 = time.time()

    sl = Solution()
    result = sl.addOperators(num, target)
#   result = sl.addOperators2(num, target)
#   result = sl.addOperators3(num, target)
#   result = sl.addOperators4(num, target)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

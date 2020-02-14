# coding: utf-8

import os
import sys
import time

class Solution:
#   def pathInZigZagTree(self, label: int) -> List[int]:
    def pathInZigZagTree(self, label):
        # 32ms
        return self.pathInZigZagTree(3 * 2 ** (len(bin(label)) - 4) - 1 - label//2) + [label] if label > 1 else [1]

    def pathInZigZagTree2(self, label):
        # 36ms
        res = []
        cur = label
        level = 0
        while cur > 0:
            level += 1
            cur >>= 1
        while label > 0:
            res.append(label)
            label = 2**level-1 + 2**(level - 1) - label
            label //= 2
            level -= 1
        return res[::-1]

    def pathInZigZagTree3(self, label):
        # 40ms
        r = []
        if label < 1:
            return r
        import math
        levels = int(math.log(label, 2)) + 1
        c_label, c_level = label, levels
        while c_level > 0:
            if c_level == levels:
                c_label = label
            else:
                if c_level % 2 == 0:
                    left, right = 2 ** (c_level - 1), 2 ** c_level - 1
                    c_label = c_label // 2
                    c_label = left + right - c_label
                else:
                    left, right = 2 ** c_level, 2 ** (c_level + 1) - 1
                    o_label = left + (right - c_label)
                    c_label = o_label // 2
            r.append(c_label)
            c_level -= 1
        r.reverse()
        return r

    def pathInZigZagTree_work(self, label):
        i = 0
        while pow(2, i) < label:
            i += 1
        i -= 1
        if i % 2 == 1:
            label = pow(2, i) + pow(2, i + 1) - (label +  1)

        result = [label]
        while True:
            label //= 2
            if label > 0:
                result = [label] + result
            else:
                break
        print("result = {0}".format(result))
        for i in range(1, len(result) - 1):
            if i % 2 == 1:
                result[i] = pow(2, i) + pow(2, i + 1) - (result[i] +  1)
        return result

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()
    label = int(flds)
    print("label = {0}".format(label))
    time0 = time.time()

    sl = Solution()
    result = sl.pathInZigZagTree(label)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

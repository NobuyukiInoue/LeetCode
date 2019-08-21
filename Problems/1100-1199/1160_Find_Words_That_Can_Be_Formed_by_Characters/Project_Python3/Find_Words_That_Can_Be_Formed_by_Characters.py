# coding: utf-8

import os
import sys
import time
from collections import Counter as cnt

class Solution:
#   def countCharacters(self, words: List[str], chars: str) -> int:
    def countCharacters(self, words, chars):
        # 112ms
        dic = {}
        for i in chars:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        dic2 = dic
        count = 0
        for i in words:
            flag = True
            dic = dic2.copy()
            if len(i) > len(chars):
                flag = False
                continue
            for j in i:
                if j in dic:
                    dic[j] -= 1
                    if dic[j] < 0:
                        flag = False
                        break
                else:
                    flag = False
            if flag:
                count += len(i)
        return count

    def countCharacters2(self, words, chars):
        # 532ms
        return sum(not cnt(w) - cnt(chars) and len(w) for w in words)

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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")
    words = flds[0].split(",")
    chars = flds[1]

    print("words = = {0}, chars = {1}".format(words, chars))
    time0 = time.time()

    sl = Solution()
    result = sl.countCharacters(words, chars)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

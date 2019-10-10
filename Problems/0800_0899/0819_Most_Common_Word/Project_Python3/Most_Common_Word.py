# coding: utf-8

import collections
import os
import re
import sys
import time

class Solution:
#    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    def mostCommonWord2(self, paragraph, banned):
        words = re.compile('\w+').findall(paragraph.lower())
        dic = {}
        for i in words:
            if(i in dic.keys()):
                dic[i] +=1
            else:
                dic[i] = 1
        for k in banned:
            dic[k] = 0
        the_word = max(dic, key = dic.get)
        return the_word

#    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    def mostCommonWord(self, paragraph, banned):
        targetStr = paragraph.replace("'", "").replace(";", "").replace(".", "").replace(", ",",").replace(","," ").replace("?","").replace("!","")

        for r_word in banned:
            targetStr = targetStr.replace(" " + r_word, "")

        targetStr = targetStr.split(" ")
        dic = {}
        max, t_key = 0, ""

        for cur in targetStr:
            cur = cur.lower()

            if cur in banned:
                continue

            if not cur in dic:
                dic[cur] = 1
            else:
                dic[cur] += 1

            if dic[cur] > max:
                t_key, max = cur, dic[cur]

        return t_key

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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").rstrip().split("],[")
    paragraph = flds[0]
    banned = flds[1].split(",")

    print("paragraph = %s" %paragraph)
    print("banner = %s" %banned)

    time0 = time.time()

    sl = Solution()
    result = sl.mostCommonWord(paragraph, banned)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()

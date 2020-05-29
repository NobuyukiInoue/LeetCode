# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
    def isPrefixOfWord(self, sentence, searchWord):
        # 20ms
        flds = sentence.split(" ")
        len_searchWord = len(searchWord)
        for i in range(len(flds)):
            if searchWord == flds[i][:len_searchWord]:
                return i + 1
        return -1

    def isPrefixOfWord2(self, sentence, searchWord):
        # 24ms
    	return next((i+1 for i,word in enumerate(sentence.split()) if word.startswith(searchWord)),-1)

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    sentence = flds[0]
    searchWord = flds[1]

    print("sentence = \"{0}\", searchWord = \"{1}\"".format(sentence, searchWord))
  
    time0 = time.time()

    sl = Solution()
    result = sl.isPrefixOfWord(sentence, searchWord)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

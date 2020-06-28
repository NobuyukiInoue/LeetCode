# coding: utf-8

import os
import sys
import time

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        results = []
        alphabet = [{'u', 'y', 't', 'r', 'q', 'o', 'w', 'p', 'e', 'i'},{'l', 'k', 'f', 's', 'j', 'g', 'a', 'h', 'd'},{'x', 'c', 'z', 'v', 'b', 'm', 'n'}]
        for word in words:
            s = set(word.lower())
            for alp in alphabet:
                if s.issubset(alp):
                    results.append(word)
                    break
        return results

    def findWords_work(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if words == None:
            return None

        words_temp = []
        for i in range(len(words)):
            words_temp.append(words[i].lower())

        key_row = [""]*3
        key_row[0] = "qwertyuiop"
        key_row[1] = "asdfghjkl"
        key_row[2] = "zxcvbnm"
        results = []

        for i in range(len(words_temp)):
            target_row = -1
            first_checked = False

            if len(words_temp[i]) == 1:
                results.append(words[i])
                continue

            for pos1 in range(len(words_temp[i])):
                if pos1 == 0:
                    for j in range(len(key_row)):
                        for pos2 in range(len(key_row[j])):
                            if words_temp[i][pos1] == key_row[j][pos2]:
                                target_row = j
                                first_checked = True
                                break
                        if first_checked:
                            break
                else:
                    isSame_row = False
                    for pos2 in range(len(key_row[target_row])):
                        if words_temp[i][pos1] == key_row[target_row][pos2]:
                            isSame_row = True
                    if isSame_row == False:
                        break
            if isSame_row:
                results.append(words[i])

        return results

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
    words = temp.replace("\"","").replace(" ","").replace("[","").replace("]","").rstrip().split(",")

    sl = Solution()
    time0 = time.time()
    result = sl.findWords(words)

    print("result = {0}".format(result))

    time1 = time.time()
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

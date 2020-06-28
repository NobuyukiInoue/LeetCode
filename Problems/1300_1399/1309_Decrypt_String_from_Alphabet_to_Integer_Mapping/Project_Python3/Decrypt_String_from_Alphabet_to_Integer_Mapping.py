# coding: utf-8

import os
import re
import sys
import time

class Solution:
#   def freqAlphabets(self, s: str) -> str:
    def freqAlphabets2(self, s):
        # 40ms
        return ''.join(chr(int(i[:2]) + 96) for i in re.findall(r'\d\d#|\d', s))

    def freqAlphabets3(self, s: str) -> str:
        # 52ms
        temp = []
        i = 0
        while i <= len(s) - 1:
            if i + 2 <= len(s) - 1 and s[i + 2] == '#':
                temp.append(chr(int(s[i:i+2]) + 96))
                i += 3
            else:
                temp.append(chr(int(s[i]) + 96 ))
                i += 1
        return ''.join(temp)

    def freqAlphabets(self, s: str) -> str:
        # 20ms
        index = 0
        ret = []
        while (index < len(s)):
            number_str = None
            if (s[index] == '1' or s[index] == '2'):
                index_t = index + 2
                if (index_t < len(s) and s[index_t] == '#'):
                    number_str = s[index] + s[index + 1]
                    index += 1
                else:
                    number_str = s[index]
            elif (s[index] != '#'):
                number_str = s[index]
            else:
                pass
            if (s[index] != '#'):
                ret.append(chr(int(number_str) + 96))
            index += 1
        return "".join(ret)


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
    s = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    sl = Solution()
    time0 = time.time()
    result = sl.freqAlphabets(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

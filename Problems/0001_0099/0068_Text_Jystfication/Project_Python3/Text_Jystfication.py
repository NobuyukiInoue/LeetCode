import os
import sys
import time

class Solution:
    def fullJustify(self, words: 'List[str]', maxWidth: 'int') -> 'List[str]':
        index, output = 0, []
        while index < len(words):
            total_len, temp = 0, []
            while index < len(words) and total_len + len(words[index]) + len(temp) <= maxWidth:
                temp.append(words[index])
                total_len += len(words[index])
                index += 1
            op, block = [] if not temp else [temp[0]], maxWidth - total_len
            for i in range(1, len(temp)):
                c = 1 if block%len(temp[i:]) else 0
                chip = 1 if index == len(words) else min(block, block//len(temp[i:]) + c)
                op.extend([" " * chip, temp[i]])
                block -= chip
            else:
                op.extend([" " * block] if block > 0 else [])
            output.append("".join(op))
        return output

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
        print("argv[1] = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    words = flds[0].split(",")
    maxwidth = int(flds[1])
    print("words[] = {0}, maxwidth = {1:d}".format(words, maxwidth))

    sl = Solution()
    time0 = time.time()

    result = sl.fullJustify(words, maxwidth)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

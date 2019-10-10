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
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()


def loop_main(temp):
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    words = str_args[0].split(",")
    maxwidth = int(str_args[1])
    print("words[] = %s, maxwidth = %d" %(words, maxwidth))

    time0 = time.time()

    sl = Solution()
    result = sl.fullJustify(words, maxwidth)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()

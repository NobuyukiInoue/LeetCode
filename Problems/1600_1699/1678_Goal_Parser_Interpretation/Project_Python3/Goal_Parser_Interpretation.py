import os
import sys
import time
from typing import List,Dict,Tuple

class Solution:
    def interpret(self, command: str) -> str:
        # 32ms
        return command.replace("(al)", "al").replace("()", "o")

    def interpret2(self, command: str) -> str:
        # 32ms
        interpreter = {'G'    : 'G',
                       '()'   : 'o',
                       '(al)' : 'al'}
        empty = ""
        final = ""
        for letter in command:
            empty += letter
            if empty in interpreter:
                final += interpreter.get(empty)
                empty = ""
        return final


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
    command = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("command = {0}".format(command))

    sl = Solution()
    time0 = time.time()

    result = sl.interpret(command)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

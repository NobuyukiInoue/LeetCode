import os
import sys
import time
import WordDictionary

def Implement_WordDictionary_Loop(ope, words):
    if len(ope) <= 0 or len(words) <= 0:
        return
    if len(ope) != len(words):
        return
    wd = WordDictionary.WordDictionary()
    for i in range(len(ope)):
        if ope[i] == "addWord":
            wd.addWord(words[i])
            print("addWord({0})".format(words[i]))
        elif ope[i] == "search":
            res = wd.search(words[i])
            print("search({0}) -> {1}".format(words[i], res))

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
    str_args = temp.replace(" ", "").replace("\"", "").rstrip().split("],[[")
    ope = str_args[0].replace("\"", "").replace("[", "").replace("]", "").split(",")

    if len(str_args) > 1:
        words = str_args[1].replace("]]]", "").split("],[")

    else:
        words = [[]]

    print("ope[] = {0}, words = {1}".format(ope, words))

    time0 = time.time()

    Implement_WordDictionary_Loop(ope, words)

    time1 = time.time()
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

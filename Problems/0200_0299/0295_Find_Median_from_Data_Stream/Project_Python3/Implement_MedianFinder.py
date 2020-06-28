import os
import sys
import time
import MedianFinder

def Implement_MedianFinder_Loop(ope, params):
    if len(ope) <= 0 or len(params) <= 0:
        return
    
    if len(ope) != len(params):
        return

    mf = MedianFinder.MedianFinder()
    for i in range(len(ope)):
        if ope[i] == "MedianFinder":
            print("MedianFinder()")

        elif ope[i] == "addNum":
            mf.addNum(int(params[i]))
            print("addNum({0})".format(params[i]))

        elif ope[i] == "findMedian":
            res = mf.findMedian()
            print("findMedian({0}) ... {1:f}".format(params[i], res))

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
        params = str_args[1].replace("]]]", "").split("],[")

    else:
        params = [[]]

    print("ope[] = {0}, params = {1}".format(ope, params))

    time0 = time.time()

    Implement_MedianFinder_Loop(ope, params)

    time1 = time.time()
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

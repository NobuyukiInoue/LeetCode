# coding: utf-8

import os
import sys
import time

import threading
from typing import List, Dict, Tuple, Callable

class ZeroEvenOdd:
    # 44ms
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.sem_zero = threading.Semaphore(1)
        self.sem_even = threading.Semaphore(0)
        self.sem_odd = threading.Semaphore(0)
        self.isFinished = False

	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.sem_zero.acquire()
            printNumber(0)
            if i % 2:
                self.sem_odd.release()
            else:
                self.sem_even.release()
        self.isFinished = True
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.sem_even.acquire()
            printNumber(i)
            self.sem_zero.release()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.sem_odd.acquire()
            printNumber(i)
            self.sem_zero.release()

    def printNumber(self, n: int):
        print("{0:d}".format(n), end="")


class Solution:
    def start_ZeroEvenOdd(self, n: int):
        zeroEvenOdd = ZeroEvenOdd(n)

        myThreads = []
        myThreads.append(threading.Thread(target=zeroEvenOdd.zero, args=([zeroEvenOdd.printNumber])))
        myThreads.append(threading.Thread(target=zeroEvenOdd.even, args=([zeroEvenOdd.printNumber])))
        myThreads.append(threading.Thread(target=zeroEvenOdd.odd, args=([zeroEvenOdd.printNumber])))

        for mt in myThreads:
            mt.start()

        while zeroEvenOdd.isFinished == False:
            time.sleep(0.05)
        print()

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
    fld = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()
    n = int(fld)
    print("n = {0:d}".format(n))

    sl = Solution()

    time0 = time.time()

    sl.start_ZeroEvenOdd(n)

    time1 = time.time()

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

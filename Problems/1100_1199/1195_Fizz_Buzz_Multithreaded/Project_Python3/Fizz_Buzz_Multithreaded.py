# coding: utf-8

import os
import sys
import time

import threading

# 32ms

class FizzBuzz(object):
#   def __init__(self, n: int):
    def __init__(self, n):
        self.n = n
        self.fz = threading.Semaphore(0)
        self.bz = threading.Semaphore(0)
        self.fzbz = threading.Semaphore(0)
        self.num = threading.Semaphore(1)

    # printFizz() outputs "fizz"
    # def fizz(self, printFizz: 'Callable[[], None]') -> None:
    def fizz(self, printFizz):
        for _ in range(self.n//3 - self.n//15):
            self.fz.acquire()
            printFizz()
            self.num.release()

    # printBuzz() outputs "buzz"
    # def buzz(self, printBuzz: 'Callable[[], None]') -> None:
    def buzz(self, printBuzz):
        for _ in range(self.n//5 - self.n//15):
            self.bz.acquire()
            printBuzz()
            self.num.release()

    # printFizzBuzz() outputs "fizzbuzz"
    # def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
    def fizzbuzz(self, printFizzBuzz):
        for _ in range(self.n//15):
            self.fzbz.acquire()
            printFizzBuzz()
            self.num.release()

    # printNumber(x) outputs "x", where x is an integer.
    # def number(self, printNumber: 'Callable[[int], None]') -> None:
    def number(self, printNumber):
        for i in range(1, self.n + 1):
            self.num.acquire()
            if i%3 == 0 and i%5 == 0:
                self.fzbz.release()
            elif i%3 == 0:
                self.fz.release()
            elif i%5 == 0:
                self.bz.release()
            else:
                printNumber(i)
                self.num.release()

    def printFizz(self):
        print(" Fizz", end="")

    def printBuzz(self):
        print(" Buzz", end="")

    def printFizzBuzz(self):
        print(" FizzBuzz", end="")

    def printNumber(self, x):
        print(" {0:d}".format(x), end="")

class Solution:
    def foobar(self, n):
        fz = FizzBuzz(n)

        myThreads = []
        myThreads.append(threading.Thread(target = fz.fizz, args = ([fz.printFizz])))
        myThreads.append(threading.Thread(target = fz.buzz, args = ([fz.printBuzz])))
        myThreads.append(threading.Thread(target = fz.fizzbuzz, args = ([fz.printFizzBuzz])))
        myThreads.append(threading.Thread(target = fz.number, args = ([fz.printNumber])))

        for mt in myThreads:
            mt.start()

        thread_list = threading.enumerate()
        thread_list.remove(threading.main_thread())
        for thread in thread_list:
            thread.join()

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    n = int(flds)
    print("n = {0}".format(n))

    sl = Solution()

    time0 = time.time()

    sl.foobar(n)

    time1 = time.time()

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

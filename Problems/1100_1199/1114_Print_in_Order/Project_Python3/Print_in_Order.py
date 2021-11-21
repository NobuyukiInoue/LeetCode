# coding: utf-8

import os
import sys
import time

import threading
from typing import List, Dict, Tuple, Callable

class Foo:
    # 28ms
    isFinished = False

    def __init__(self):
        self.sem_second = threading.Semaphore(0)
        self.sem_third = threading.Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.sem_second.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self.sem_second:
            printSecond()
            self.sem_third.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self.sem_third:
            printThird()

    def printFirst(self):
        print("first", end="")

    def printSecond(self):
        print("second", end="")

    def printThird(self):
        print("third", end="")
        self.isFinished = True

class Solution:
    def fooStart(self, nums: List[int]):
        foo = Foo()

        myThreads = []
        for num in nums:
            if num == 1:
                myThreads.append(threading.Thread(target=foo.first, args=([foo.printFirst])))
            elif num == 2:
                myThreads.append(threading.Thread(target=foo.second, args=([foo.printSecond])))
            elif num == 3:
                myThreads.append(threading.Thread(target=foo.third, args=([foo.printThird])))

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
    nums = [int(_) for _ in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()

    time0 = time.time()

    sl.fooStart(nums)

    time1 = time.time()

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

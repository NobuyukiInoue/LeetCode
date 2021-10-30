# coding: utf-8

import os
import sys
import time

import threading

class FooBar:
    # 56ms
    def __init__(self, n):
        self.n = n
        self.foosema = threading.Semaphore(1)
        self.barsema = threading.Semaphore(0)

    def foo(self, printFoo):
        for i in range(self.n):
            self.foosema.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.barsema.release()

    def bar(self, printBar):
        for i in range(self.n):
            self.barsema.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foosema.release()

    def printFoo(self):
        print("foo", end="")

    def printBar(self):
        print("bar", end="")

class FooBar2:
    # 120ms
    def __init__(self, n: int):
        self.n = n
        self.foo_printed = False
        self.condition = threading.Condition()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
       for i in range(self.n):
            with self.condition:
                self.condition.wait_for(
                    lambda: not self.foo_printed
                )
                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
                self.foo_printed = True
                self.condition.notifyAll()
    
    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.condition:
                self.condition.wait_for(
                    lambda: self.foo_printed
                )
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()
                self.foo_printed = False
                self.condition.notifyAll()

    def printFoo(self):
        print("foo", end="")

    def printBar(self):
        print("bar", end="")

class Solution:
    def foobar(self, n):
        fb = FooBar(n)

        myThreads = []
        myThreads.append(threading.Thread(target=fb.foo, args=([fb.printFoo])))
        myThreads.append(threading.Thread(target=fb.bar, args=([fb.printBar])))

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

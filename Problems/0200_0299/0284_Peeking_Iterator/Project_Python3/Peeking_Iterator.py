import os
import sys
import time

class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.list = nums
        self.index = 0

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        if self.index < len(self.list) - 1:
            return True
        return False

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        res = self.list[self.index]
        if self.hasNext():
            self.index += 1
        return res

class PeekingIterator:
    # 24ms
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._iterator = iterator
        self.cache = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.cache:
            self.cache = self._iterator.next()
        return self.cache

    def next(self):
        """
        :rtype: int
        """
        if self.cache: 
            val, self.cache = self.cache, None
            return val
        return self._iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._iterator.hasNext() or self.cache != None


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].


class Solution:
    def main(self, cmds, args):
        res = []
        for i in range(len(cmds)):
            if cmds[i] == "PeekingIterator":
                peekingIterator = PeekingIterator(Iterator(args[i]))
                res.append(None)
                print("Exec PeekingIterator().")

            else:
                if peekingIterator is None:
                    print("peekingIterator not found... {0}".format(cmds[i]))
                    exit(1)

                elif cmds[i] == "peek":
                    res.append(peekingIterator.peek())
                    print("peek() ... {0}".format(res[-1]))

                elif cmds[i] == "next":
                    res.append(peekingIterator.next())
                    print("next() ... {0}".format(res[-1]))

                elif cmds[i] == "hasNext":
                    res.append(peekingIterator.hasNext())
                    print("hasNext() ... {0}".format(res[-1]))

                else:
                    print("error... {0}".format(cmds[i]))
                    exit(1)
        return res

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
    flds = temp.replace("\"","").replace(", ",",").rstrip().split("],[[")
    cmds = flds[0].replace("[", "").replace("]", "").split(",")
    args = flds[1].replace("]]]]","").split("],[")
    print(args)
    args[0] = [int(_) for _ in args[0].replace("[", "").replace("]", "").split(",")]

    print("cmds[] = {0}".format(cmds))
    print("args[] = {0}".format(args))

    sl = Solution()
    time0 = time.time()
    result = sl.main(cmds, args)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

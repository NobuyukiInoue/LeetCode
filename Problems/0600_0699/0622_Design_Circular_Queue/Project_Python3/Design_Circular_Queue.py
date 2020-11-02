import os
import sys
import time


class MyCircularQueue:
    # 68ms

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.maxlen = k
        self.currlen = 0
        self.queue = [None] * k
        self.head = -1
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        
        tail = (self.tail+1) % self.maxlen
        self.queue[tail] = value
        self.tail = tail
        self.currlen += 1
        if self.currlen == 1:
            self.head = 0
        return True
    
    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        
        self.head = (self.head+1) % self.maxlen
        self.currlen -= 1
        if self.isEmpty():
            self.head = -1
            self.tail = -1
                
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        
        return self.queue[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.currlen == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.currlen == self.maxlen


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

class Solution:
    def main(self, cmds, args):
        ans = []
        for i in range(len(cmds)):
            if cmds[i] == "MyCircularQueue":
                circularQueue = MyCircularQueue(args[i])
                print("Exec circularQueue({0}).".format(args[i]))
                ans.append(None)
            else:
                if circularQueue is None:
                    print("circularQueue not found... {0}".format(cmds[i]))
                    exit(1)

                elif cmds[i] == "enQueue":
                    res = circularQueue.enQueue(args[i])
                    print("circularQueue.enQueue({0}) ... {1}".format(args[i], res))
                    ans.append(res)

                elif cmds[i] == "deQueue":
                    res = circularQueue.deQueue()
                    print("circularQueue.deQueue() ... {0}".format(res))
                    ans.append(res)

                elif cmds[i] == "Front":
                    res = circularQueue.Front()
                    print("circularQueue.Front() ... {0}".format(res))
                    ans.append(res)

                elif cmds[i] == "Rear":
                    res = circularQueue.Rear()
                    print("circularQueue.Rear() ... {0}".format(res))
                    ans.append(res)

                elif cmds[i] == "isEmpty":
                    res = circularQueue.isEmpty()
                    print("circularQueue.isEmpty() ... {0}".format(res))
                    ans.append(res)

                elif cmds[i] == "isFull":
                    res = circularQueue.isFull()
                    print("circularQueue.isFull() ... {0}".format(res))
                    ans.append(res)

                else:
                    print("error... {0}".format(cmds[i]))
                    exit(1)
        return ans

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
    cmds = flds[0].replace("[[", "").split(",")
    args = flds[1].replace("]]]","").split("],[")
    for i, _ in enumerate(args):
        if args[i].isnumeric():
            args[i] = int(args[i])

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

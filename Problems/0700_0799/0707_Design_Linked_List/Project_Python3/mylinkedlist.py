class MyLinkedList:

    def __init__(self):
        self.coll=[]

    def get(self, index):
        if len(self.coll) <= index or index < 0:
            return -1
        return self.coll[index]

    def addAtHead(self, val):
        self.coll = [val] + self.coll

    def addAtTail(self, val):
        self.coll += [val]

    def addAtIndex(self, index, val):
        if index <= len(self.coll):
            self.coll = self.coll[:index] + [val] + self.coll[index:]

    def deleteAtIndex(self, index):
        self.coll = self.coll[:index] + self.coll[index+1:]

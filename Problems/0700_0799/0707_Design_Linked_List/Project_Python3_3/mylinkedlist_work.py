class MyLinkedList:
    class LinkedList:
        def __init__(self, val):
            self.Val = val
            self.next = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = self.LinkedList(None)

    def get(self, index: 'int') -> 'int':
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        curr = self.head
        s_index = 0
        while s_index < index:
            if  curr.next == None:
                return -1
            curr = curr.next
            s_index += 1

        if curr.Val != None:
            return curr.Val
        else:
            return -1

    def addAtHead(self, val: 'int') -> 'None':
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head.Val == None:
            self.head.Val = val
        else:
            curr = self.head
            node = self.LinkedList(val)
            node.next = curr
            self.head = node

    def addAtTail(self, val: 'int') -> 'None':
        """
        Append a node of value val to the last element of the linked list.
        """
        curr = self.head
        while curr.next != None:
            curr = curr.next

        curr.next = self.LinkedList(val)

    def addAtIndex(self, index: 'int', val: 'int') -> 'None':
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            node = self.LinkedList(val)
            node.next = self.head
            self.head = node
            return

        curr = self.head
        s_index = 0

        while s_index < index - 1:
            curr = curr.next
            s_index += 1

        temp = curr.next
        if curr != None:
            if curr.Val != None:
                node = self.LinkedList(val)
                curr.next = node
                node.next = temp

    def deleteAtIndex(self, index: 'int') -> 'None':
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self.head = self.head.next
            return

        curr = self.head
        s_index = 0
        while s_index < index - 1:
            curr = curr.next
            s_index += 1

        if curr.next != None:
            if curr.next.next != None:
                curr.next = curr.next.next
            else:
                curr.next = None
            

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

    def print_LinkedList(self):
        if self.head == None:
            return ""

        resultStr = str(self.head.Val)
        node = self.head
        while node.next != None:
            resultStr += " -> " + str(node.next.Val)
            node = node.next

        return resultStr

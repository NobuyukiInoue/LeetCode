package mylinkedlistSubmission

import (
	"reflect"
	"strconv"
)

// MyLinkedList Singly linked list.
type MyLinkedList struct {
	val  int
	next *MyLinkedList
}

// Constructor Initialize your data structure here.
func Constructor() MyLinkedList {
	return MyLinkedList{}
}

// Get the value of the index-th node in the linked list. If the index is invalid, return -1.
func (myLinkedList *MyLinkedList) Get(index int) int {
	linkedList := *myLinkedList
	for i := 0; i < index; i++ {
		if reflect.DeepEqual(linkedList, MyLinkedList{}) {
			return -1
		}
		linkedList = *linkedList.next
	}

	if reflect.DeepEqual(linkedList, MyLinkedList{}) {
		return -1
	}
	return linkedList.val
}

// AddAtHead Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
func (myLinkedList *MyLinkedList) AddAtHead(val int) {
	nextLinkedList := *myLinkedList
	*myLinkedList = MyLinkedList{val, &nextLinkedList}
}

// AddAtTail Append a node of value val to the last element of the linked list.
func (myLinkedList *MyLinkedList) AddAtTail(val int) {
	linkedList := *myLinkedList
	for !reflect.DeepEqual(*linkedList.next, MyLinkedList{}) {
		linkedList = *linkedList.next
	}

	*linkedList.next = MyLinkedList{val, &MyLinkedList{}}
}

// AddAtIndex Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
func (myLinkedList *MyLinkedList) AddAtIndex(index int, val int) {
	linkedListPtr := myLinkedList
	for i := 0; i < index; i++ {
		if reflect.DeepEqual(*linkedListPtr, MyLinkedList{}) {
			return
		}
		linkedListPtr = linkedListPtr.next
	}

	nextLinkedList := *linkedListPtr
	*linkedListPtr = MyLinkedList{val, &nextLinkedList}
}

// DeleteAtIndex Delete the index-th node in the linked list, if the index is valid.
func (myLinkedList *MyLinkedList) DeleteAtIndex(index int) {
	linkedListPtr := myLinkedList
	for i := 0; i < index; i++ {
		if (reflect.DeepEqual(*linkedListPtr, MyLinkedList{})) {
			return
		}
		linkedListPtr = linkedListPtr.next
	}

	if linkedListPtr == nil {
		return
	}

	if linkedListPtr.next == nil {
		*linkedListPtr = MyLinkedList{}
		return
	}
	*linkedListPtr = *linkedListPtr.next
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Get(index);
 * obj.AddAtHead(val);
 * obj.AddAtTail(val);
 * obj.AddAtIndex(index,val);
 * obj.DeleteAtIndex(index);
 */

func (this *MyLinkedList) MyLinkedListStr() string {
	if this == nil {
		return ""
	}

	curr := this
	resultStr := strconv.Itoa(this.val)

	for curr.next != nil {
		curr = curr.next
		resultStr += "," + strconv.Itoa(curr.val)
	}

	return resultStr
}

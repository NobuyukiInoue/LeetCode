package mylinkedlist

import "strconv"

type MyLinkedList struct {
	val  int
	next *MyLinkedList
}

/** Initialize your data structure here. */
func Constructor() MyLinkedList {
	return MyLinkedList{}
}

/** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
func (this *MyLinkedList) Get(index int) int {
	if index < 0 {
		return -1
	}

	curr := this
	depth := 0
	for ; depth < index; depth++ {
		if curr.next == nil {
			break
		}

		curr = curr.next
	}

	if depth == index {
		return curr.val
	} else {
		return -1
	}
}

/** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
func (this *MyLinkedList) AddAtHead(val int) {
	next := *this
	*this = MyLinkedList{val, &next}
}

/** Append a node of value val to the last element of the linked list. */
func (this *MyLinkedList) AddAtTail(val int) {
	curr := this
	for curr.next != nil {
		curr = curr.next
	}

	node := MyLinkedList{val, nil}
	curr.next = &node
}

/** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
func (this *MyLinkedList) AddAtIndex(index int, val int) {
	if index < 0 {
		return
	}

	curr := this
	for depth := 0; depth < index-1; depth++ {
		if curr.next == nil {
			return
		}

		curr = curr.next
	}

	node := MyLinkedList{val, curr.next}
	curr.next = &node
}

/** Delete the index-th node in the linked list, if the index is valid. */
func (this *MyLinkedList) DeleteAtIndex(index int) {
	curr := this
	for depth := 0; depth < index-1; depth++ {
		if curr.next == nil {
			return
		}

		curr = curr.next
	}

	if curr.next != nil {
		if curr.next.next != nil {
			curr.next = curr.next.next
		}
	}
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

func (this *MyLinkedList) FirstSet(val int) {
	this.val = val
	this.next = nil
}

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

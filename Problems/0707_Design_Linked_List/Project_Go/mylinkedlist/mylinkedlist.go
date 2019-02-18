package mylinkedlist

type MyLinkedList struct {
	Val  int
	Next *MyLinkedList
}

/** Initialize your data structure here. */
func Constructor() MyLinkedList {
	return MyLinkedList{}
}

/** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
func (this *MyLinkedList) Get(index int) int {
	curr := this
	for s_index := 1; s_index < index; s_index++ {
		curr = curr.Next
	}

	return curr.Val
}

/** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
func (this *MyLinkedList) AddAtHead(val int) {
	curr := this
	this.Val = val
	if curr != nil {
		this.Next = curr
	}
}

/** Append a node of value val to the last element of the linked list. */
func (this *MyLinkedList) AddAtTail(val int) {
	curr := this
	for curr.Next != nil {
		curr = curr.Next
	}
	curr.Next = new(MyLinkedList)
	curr.Next.Val = val
}

/** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
func (this *MyLinkedList) AddAtIndex(index int, val int) {
	curr := this
	for s_index := 1; s_index < index; s_index++ {
		curr = curr.Next
	}

	temp := curr
	curr.Val = val
	curr.Next = temp
}

/** Delete the index-th node in the linked list, if the index is valid. */
func (this *MyLinkedList) DeleteAtIndex(index int) {
	curr := this
	for s_index := 1; s_index < index-1; s_index++ {
		curr = curr.Next
	}

	if curr.Next.Next != nil {
		curr.Next = curr.Next.Next
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

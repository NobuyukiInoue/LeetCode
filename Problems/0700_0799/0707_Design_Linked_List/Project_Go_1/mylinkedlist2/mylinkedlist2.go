package mylinkedlist2

import (
	"strconv"
)

type MyLinkedList struct {
	coll []int
}

/** Initialize your data structure here. */
func Constructor() MyLinkedList {
	return MyLinkedList{}
}

/** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
func (this *MyLinkedList) Get(index int) int {
	if len(this.coll) <= index || index < 0 {
		return -1
	}

	return this.coll[index]
}

/** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
func (this *MyLinkedList) AddAtHead(val int) {
	this.coll = append([]int{val}, this.coll...)
}

/** Append a node of value val to the last element of the linked list. */
func (this *MyLinkedList) AddAtTail(val int) {
	this.coll = append(this.coll, val)
}

/** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
func (this *MyLinkedList) AddAtIndex(index int, val int) {
	if index <= len(this.coll) {
		/*
			coll1 := this.coll[:index]
			coll2 := this.coll[index:]
		*/
		/*
			coll1, _ := slicecopy(this.coll, 0, index)
			coll2, _ := slicecopy(this.coll, index, len(this.coll))
		*/
		coll1 := make([]int, index)
		copy(coll1, this.coll[0:index])
		coll2 := make([]int, len(this.coll)-index)
		copy(coll2, this.coll[index:len(this.coll)])

		coll_new := append(coll1, val)
		this.coll = append(coll_new, coll2...)
	}
}

/** Delete the index-th node in the linked list, if the index is valid. */
func (this *MyLinkedList) DeleteAtIndex(index int) {
	/*
		coll1 := this.coll[:index]
		coll2 := this.coll[index+1:]
	*/
	/*
		coll1, _ := slicecopy(this.coll, 0, index)
		coll2, _ := slicecopy(this.coll, index+1, len(this.coll))
	*/
	if index >= len(this.coll) {
		return
	}

	coll1 := make([]int, index)
	copy(coll1, this.coll[0:index])
	coll2 := make([]int, len(this.coll)-(index+1))
	copy(coll2, this.coll[index+1:len(this.coll)])

	this.coll = append(coll1, coll2...)
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

func (this *MyLinkedList) Coll() string {
	if len(this.coll) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(this.coll[0])
	for i := 1; i < len(this.coll); i++ {
		resultStr += ", " + strconv.Itoa(this.coll[i])
	}

	return resultStr
}

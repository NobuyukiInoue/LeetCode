package mylinkedlist

import (
	"fmt"
	"strconv"
)

type MyLinkedList struct {
	value []int
}

/** Initialize your data structure here. */
func Constructor() MyLinkedList {
	return MyLinkedList{}
}

/** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
func (this *MyLinkedList) Get(index int) int {
	if len(this.value) <= index || index < 0 {
		return -1
	}

	return this.value[index]
}

/** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
func (this *MyLinkedList) AddAtHead(val int) {
	this.value = append([]int{val}, this.value...)
}

/** Append a node of value val to the last element of the linked list. */
func (this *MyLinkedList) AddAtTail(val int) {
	this.value = append(this.value, val)
}

/** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
func (this *MyLinkedList) AddAtIndex(index int, val int) {
	if index <= len(this.value) {
		value1, _ := slicecopy(this.value, 0, index)
		value2, _ := slicecopy(this.value, index, len(this.value))
		value_new := append(value1, val)
		this.value = append(value_new, value2...)
	}
}

/** Delete the index-th node in the linked list, if the index is valid. */
func (this *MyLinkedList) DeleteAtIndex(index int) {
	if index >= len(this.value) {
		return
	}

	value1, _ := slicecopy(this.value, 0, index)
	value2, _ := slicecopy(this.value, index+1, len(this.value))
	this.value = append(value1, value2...)
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

func slicecopy(slice []int, start int, end int) ([]int, error) {
	if len(slice) < start || len(slice) < end {
		return nil, fmt.Errorf("Error")
	}

	ans := make([]int, (end - start))
	copy(ans, slice[start:end])
	return ans, nil
}

func (this *MyLinkedList) GetAllvalues() string {
	if len(this.value) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(this.value[0])
	for i := 1; i < len(this.value); i++ {
		resultStr += ", " + strconv.Itoa(this.value[i])
	}

	return resultStr
}

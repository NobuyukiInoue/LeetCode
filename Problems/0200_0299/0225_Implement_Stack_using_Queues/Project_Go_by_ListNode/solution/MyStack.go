package solution

// 0ms

type ListNode struct {
	Val  int
	Next *ListNode
}

type MyStack struct {
	Node   *ListNode
	Length int
}

/** Initialize your data structure here. */
func Constructor() MyStack {
	return MyStack{nil, 0}
}

/** Push element x onto stack. */
func (this *MyStack) Push(x int) {
	if this.Node == nil {
		this.Node = &ListNode{x, nil}
	} else {
		nextNode := *this.Node
		*this.Node = ListNode{x, &nextNode}
	}
	this.Length++
}

/** Removes the element on top of the stack and returns that element. */
func (this *MyStack) Pop() int {
	if this.Node == nil {
		return 0
	}

	retVal := this.Node.Val
	if this.Node.Next != nil {
		*this.Node = *this.Node.Next
	} else {
		this.Node = nil
	}
	this.Length--

	return retVal
}

/** Get the top element. */
func (this *MyStack) Top() int {
	if this.Node == nil {
		return 0
	}

	return this.Node.Val
}

/** Returns whether the stack is empty. */
func (this *MyStack) Empty() bool {
	if this.Node == nil {
		return true
	}

	return false
}

/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */

package solution

// 0ms

type MyStack struct {
	Segment []int
	Index int
}

/** Initialize your data structure here. */
func Constructor() MyStack {
	return MyStack{make([]int, 65536), -1}
}

/** Push element x onto stack. */
func (this *MyStack) Push(x int) {
	this.Index++
	this.Segment[this.Index] = x
}

/** Removes the element on top of the stack and returns that element. */
func (this *MyStack) Pop() int {
	item := this.Segment[this.Index]
	this.Index--

	return item
}

/** Get the top element. */
func (this *MyStack) Top() int {
	if this.Index < 0 {
		return 0
	}

	return this.Segment[this.Index]
}

/** Returns whether the stack is empty. */
func (this *MyStack) Empty() bool {
	return this.Index < 0
}

/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */

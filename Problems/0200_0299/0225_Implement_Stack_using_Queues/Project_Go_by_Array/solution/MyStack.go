package solution

// 0ms

type MyStack struct {
	Nodes []int
}

/** Initialize your data structure here. */
func Constructor() MyStack {
	this := MyStack{}
	return this
}

/** Push element x onto stack. */
func (this *MyStack) Push(x int) {
	this.Nodes = append(this.Nodes, x)
	this.Nodes[0], this.Nodes[len(this.Nodes)-1] = this.Nodes[len(this.Nodes)-1], this.Nodes[0]
}

/** Removes the element on top of the stack and returns that element. */
func (this *MyStack) Pop() int {
	item := this.Nodes[0]
	this.Nodes[0], this.Nodes[len(this.Nodes)-1] = this.Nodes[len(this.Nodes)-1], this.Nodes[0]
	this.Nodes = this.Nodes[:len(this.Nodes)-1]
	return item
}

/** Get the top element. */
func (this *MyStack) Top() int {
	return this.Nodes[0]
}

/** Returns whether the stack is empty. */
func (this *MyStack) Empty() bool {
	return len(this.Nodes) == 0
}

/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */

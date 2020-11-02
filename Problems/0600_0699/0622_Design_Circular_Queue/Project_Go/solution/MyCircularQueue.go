package solution

// 8ms

type MyCircularQueue struct {
	maxlen  int
	currlen int
	queue   []int
	head    int
	tail    int
}

/** Initialize your data structure here. Set the size of the queue to be k. */
func Constructor(k int) MyCircularQueue {
	mc := new(MyCircularQueue)
	mc.maxlen = k
	mc.currlen = 0
	mc.queue = make([]int, k)
	mc.head = -1
	mc.tail = -1
	return *mc
}

/** Insert an element into the circular queue. Return true if the operation is successful. */
func (this *MyCircularQueue) EnQueue(value int) bool {
	if this.IsFull() {
		return false
	}
	this.tail = (this.tail + 1) % this.maxlen
	this.queue[this.tail] = value
	this.currlen++
	if this.currlen == 1 {
		this.head = 0
	}
	return true
}

/** Delete an element from the circular queue. Return true if the operation is successful. */
func (this *MyCircularQueue) DeQueue() bool {
	if this.IsEmpty() {
		return false
	}
	this.head = (this.head + 1) % this.maxlen
	this.currlen--
	if this.IsEmpty() {
		this.head = -1
		this.tail = -1
	}
	return true
}

/** Get the front item from the queue. */
func (this *MyCircularQueue) Front() int {
	if this.IsEmpty() {
		return -1
	}
	return this.queue[this.head]
}

/** Get the last item from the queue. */
func (this *MyCircularQueue) Rear() int {
	if this.IsEmpty() {
		return -1
	}
	return this.queue[this.tail]
}

/** Checks whether the circular queue is empty or not. */
func (this *MyCircularQueue) IsEmpty() bool {
	return this.currlen == 0
}

/** Checks whether the circular queue is full or not. */
func (this *MyCircularQueue) IsFull() bool {
	return this.currlen == this.maxlen
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * obj := Constructor(k);
 * param_1 := obj.EnQueue(value);
 * param_2 := obj.DeQueue();
 * param_3 := obj.Front();
 * param_4 := obj.Rear();
 * param_5 := obj.IsEmpty();
 * param_6 := obj.IsFull();
 */

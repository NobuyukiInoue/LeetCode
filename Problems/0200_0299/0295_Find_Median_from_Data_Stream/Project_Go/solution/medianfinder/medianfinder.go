package medianfinder

import "container/heap"

// 96ms

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type MedianFinder struct {
	large, small *IntHeap
}

/** initialize your data structure here. */
func Constructor() MedianFinder {
	// h := &IntHeap{}
	a := &IntHeap{}
	b := &IntHeap{}
	heap.Init(a)
	heap.Init(b)
	return MedianFinder{a, b}
}

func (this *MedianFinder) AddNum(num int) {
	if this.large.Len() == 0 || num > (*this.large)[0] {
		heap.Push(this.large, num)
	} else {
		heap.Push(this.small, -num)
	}
	if this.large.Len() > this.small.Len()+1 {
		heap.Push(this.small, -heap.Pop(this.large).(int))
	} else if this.small.Len() > this.large.Len()+1 {
		heap.Push(this.large, -heap.Pop(this.small).(int))
	}
}

func (this *MedianFinder) FindMedian() float64 {
	if this.large.Len() < this.small.Len() {
		return float64(-(*this.small)[0])
	} else if this.large.Len() > this.small.Len() {
		return float64((*this.large)[0])
	}
	return float64(-(*this.small)[0]+(*this.large)[0]) / 2
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(num);
 * param_2 := obj.FindMedian();
 */

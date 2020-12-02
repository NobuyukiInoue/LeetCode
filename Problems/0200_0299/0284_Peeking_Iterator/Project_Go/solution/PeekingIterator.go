package solution

// 0ms

type PeekingIterator struct {
	myIterator []int
	cache int
}

func Constructor(iter *Iterator) *PeekingIterator {
	var this PeekingIterator
	for iter.hasNext() {
		this.myIterator = append(this.myIterator, iter.next())
	}	
	this.cache = 0
	return &this
}

func (this *PeekingIterator) hasNext() bool {
	return this.cache < len(this.myIterator)
}

func (this *PeekingIterator) next() int {
	this.cache++
	return this.myIterator[this.cache - 1]
}

func (this *PeekingIterator) peek() int {
	return this.myIterator[this.cache]
}

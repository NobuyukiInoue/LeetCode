package solution

type Iterator struct {
   list []int
   index int
}

func (this *Iterator) hasNext() bool {
	// Returns true if the iteration has more elements.
	if this.index < len(this.list) {
		return true
	}
	return false
}

func (this *Iterator) next() int {
	// Returns the next element in the iteration.
	res := this.list[this.index]
	if this.hasNext() {
		this.index++
	}
	return res
}

package solution

// 72ms

type OrderedStream struct {
	stream []string
	currentIndex int
}

func Constructor(n int) OrderedStream {
	return OrderedStream{ make([]string, n), 0}
}


func (this *OrderedStream) Insert(id int, value string) []string {
	this.stream[id - 1] = value
	var res []string
	var i int

	for i = this.currentIndex; i < len(this.stream); i++ {
		if len(this.stream[i]) <= 0 {
			break
		}

		res = append(res, this.stream[i])
	}
	this.currentIndex = i

	return res
}


/**
 * Your OrderedStream object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Insert(id,value);
 */

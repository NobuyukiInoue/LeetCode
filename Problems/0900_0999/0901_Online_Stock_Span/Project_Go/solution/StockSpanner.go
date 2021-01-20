package solution

// 172ms

type StockSpanner struct {
	stack [][]int
}

func Constructor() StockSpanner {
	return StockSpanner{ make([][]int, 0) }
}

func (this *StockSpanner) Next(price int) int {
	res := 1
	stackSize := len(this.stack)
	for stackSize > 0 && this.stack[stackSize - 1][0] <= price {
		res += this.stack[stackSize - 1][1]
		this.stack = this.stack[:stackSize - 1]
		stackSize = len(this.stack)
	}
	this.stack = append(this.stack, []int {price, res})
	return res
}


/**
 * Your StockSpanner object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Next(price);
 */

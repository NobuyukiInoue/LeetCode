package solution

import (
	"math/rand"
)

// 2ms - 3ms
type Solution struct {
	nodes   [][2]int
	hash    map[[2]int]bool
	row     int
	col     int
	useHash bool
}

func Constructor(m int, n int) Solution {
	useHash := false
	nodes := make([][2]int, 0)
	hash := map[[2]int]bool{}
	if m*n > 10000 {
		useHash = true
	} else {
		for r := 0; r < m; r++ {
			for c := 0; c < n; c++ {
				nodes = append(nodes, [...]int{r, c})
			}
		}
	}
	return Solution{
		nodes:   nodes,
		hash:    hash,
		row:     m,
		col:     n,
		useHash: useHash,
	}
}

func (this *Solution) Flip() []int {
	value := make([]int, 2)
	if this.useHash {
		for {
			r := rand.Intn(this.row)
			c := rand.Intn(this.col)
			if this.hash[[...]int{r, c}] == false {
				this.hash[[...]int{r, c}] = true
				value[0] = r
				value[1] = c
				break
			}
		}
	} else {
		index := rand.Intn(len(this.nodes))
		value[0] = this.nodes[index][0]
		value[1] = this.nodes[index][1]
		copy(this.nodes[index:], this.nodes[index+1:])
		this.nodes = this.nodes[:len(this.nodes)-1]
	}
	return value
}

func (this *Solution) Reset() {
	if this.useHash {
		this.hash = map[[2]int]bool{}
	} else {
		this.nodes = make([][2]int, 0, this.row*this.col)
		for r := 0; r < this.row; r++ {
			for c := 0; c < this.col; c++ {
				this.nodes = append(this.nodes, [...]int{r, c})
			}
		}
	}
}

/*
// runtime: out of memory.

// type RandomFlipMatrix struct {
type RandomFlipMatrix struct {
	row   int
	col   int
	limit int
	used  map[int]int
}

func Constructor(m int, n int) RandomFlipMatrix {
	limit := m * n
	used := make(map[int]int, limit)
	rand.Seed(time.Now().UnixNano())
	return RandomFlipMatrix{m, n, limit, used}
}

func (this *RandomFlipMatrix) Flip() []int {
	var r, x int
	r = rand.Intn(this.limit)
	this.limit--
	if this.used[r] == 0 {
		x = r
	} else {
		x = this.used[r]
	}
	if this.used[this.limit] == 0 {
		this.used[r] = this.limit
	} else {
		this.used[r] = this.used[this.limit]
	}
	return []int{x / this.col, x % this.col}
}

func (this *RandomFlipMatrix) Reset() {
	this.limit = this.row * this.col
	this.used = make(map[int]int, this.limit)
}
*/

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(m, n);
 * param_1 := obj.Flip();
 * obj.Reset();
 */

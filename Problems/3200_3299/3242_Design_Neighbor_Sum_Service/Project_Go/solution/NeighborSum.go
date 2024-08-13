package solution

// 50ms

type NeighborSum struct {
	grid *[][]int
	n    int
	pos  map[int][]int
}

func Constructor(grid [][]int) NeighborSum {
	n := len(grid)
	nei := NeighborSum{&grid, n, nil}
	nei.pos = make(map[int][]int, 0)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			nei.pos[grid[i][j]] = []int{i, j}
		}
	}
	return nei
}

func (this *NeighborSum) AdjacentSum(value int) int {
	temp := this.pos[value]
	x, y := temp[0], temp[1]
	dirr := [][]int{{x - 1, y}, {x + 1, y}, {x, y - 1}, {x, y + 1}}
	total := 0
	for _, dir := range dirr {
		if 0 <= dir[0] && dir[0] < this.n && 0 <= dir[1] && dir[1] < this.n {
			total += (*this.grid)[dir[0]][dir[1]]
		}
	}
	return total
}

func (this *NeighborSum) DiagonalSum(value int) int {
	temp := this.pos[value]
	x, y := temp[0], temp[1]
	dirr := [][]int{{x - 1, y - 1}, {x - 1, y + 1}, {x + 1, y - 1}, {x + 1, y + 1}}
	total := 0
	for _, dir := range dirr {
		if 0 <= dir[0] && dir[0] < this.n && 0 <= dir[1] && dir[1] < this.n {
			total += (*this.grid)[dir[0]][dir[1]]
		}
	}
	return total
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * obj := Constructor(grid);
 * param_1 := obj.AdjacentSum(value);
 * param_2 := obj.DiagonalSum(value);
 */

package nummatrix

import "fmt"

type NumMatrix struct {
	sum [][]int
}

func Constructor(matrix [][]int) NumMatrix {
	nm := new(NumMatrix)
	h := len(matrix)
	nm.sum = make([][]int, len(matrix))

	if len(matrix) < 1 {
		return *nm
	}

	if len(matrix[0]) < 1 {
		return *nm
	}

	w := len(matrix[0])
	for i := 0; i < h; i++ {
		nm.sum[i] = make([]int, w)
	}

	for i := 0; i < h; i++ {
		tmp := 0
		for j := 0; j < w; j++ {
			tmp2 := 0
			if i != 0 {
				tmp2 = nm.sum[i-1][j]
			}
			nm.sum[i][j] = tmp + matrix[i][j] + tmp2
			tmp += matrix[i][j]
		}
	}

	return *nm
}

func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
	blk1 := 0
	if row1 != 0 {
		blk1 = this.sum[row1-1][col2]
	}
	blk2 := 0
	if col1 != 0 {
		blk2 = this.sum[row2][col1-1]
	}
	blk3 := 0
	if row1 != 0 && col1 != 0 {
		blk3 = this.sum[row1-1][col1-1]
	}
	blk4 := this.sum[row2][col2]

	return blk4 - blk1 - blk2 + blk3
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * obj := Constructor(matrix);
 * param_1 := obj.SumRegion(row1,col1,row2,col2);
 */

func (this *NumMatrix) PrintMatrix() {
	fmt.Printf("[\n")
	for i := 0; i < len(this.sum); i++ {
		fmt.Printf(" [")
		for j := 0; j < len(this.sum[i]); j++ {
			fmt.Printf(" %d", this.sum[i][j])
		}
		fmt.Printf(" ]\n")
	}
	fmt.Printf("]\n")
}

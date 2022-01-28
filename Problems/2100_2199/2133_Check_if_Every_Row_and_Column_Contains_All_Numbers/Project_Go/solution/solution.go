package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

type Bitset struct {
	bits   []uint64
	length int
}

func makeBitset(length int) *Bitset {
	return &Bitset{bits: make([]uint64, (length+63)/64), length: length}
}

func (b *Bitset) Set(n int) {
	b.bits[n/64] |= 1 << (n % 64)
}

func (b *Bitset) IsFilledUp() bool {
	length := b.length / 64
	for i := 0; i < length; i++ {
		if b.bits[i] != 0xffffffffffffffff {
			return false
		}
	}

	if b.length%64 > 0 {
		return b.bits[length] == 1<<(b.length%64)-1
	}

	return true
}

func (b *Bitset) Clear() {
	for i := 0; i < len(b.bits); i++ {
		b.bits[i] = 0
	}
}

func checkValid(matrix [][]int) bool {
	// 104ms
	bitset := makeBitset(len(matrix) * 2)

	for i := 0; i < len(matrix); i++ {
		bitset.Clear()

		for j := 0; j < len(matrix); j++ {
			bitset.Set(matrix[i][j] - 1)
			bitset.Set(matrix[j][i] - 1 + len(matrix))
		}

		if !bitset.IsFilledUp() {
			return false
		}
	}

	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_mat := strings.Split(flds, "],[")
	matrix := make([][]int, len(str_mat))
	for i := 0; i < len(str_mat); i++ {
		matrix[i] = StringToIntArray(str_mat[i])
	}
	fmt.Printf("matrix = %s\n", IntIntArrayToGridString(matrix))

	timeStart := time.Now()

	result := checkValid(matrix)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

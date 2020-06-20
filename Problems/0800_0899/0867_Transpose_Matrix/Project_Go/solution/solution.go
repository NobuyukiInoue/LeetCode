package solution

import (
	"fmt"
	"strings"
	"time"
)

func transpose(A [][]int) [][]int {
	rowNum := len(A)
	colNum := len(A[0])

	ret := make([][]int, colNum)
	for index := range ret {
		ret[index] = make([]int, rowNum)
	}

	for i := 0; i < colNum; i++ {
		for j := 0; j < rowNum; j++ {
			ret[i][j] = A[j][i]
		}
	}
	return ret
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	A := make([][]int, len(flds))
	for i := 0; i < len(flds); i++ {
		A[i] = StringToIntArray(flds[i])
	}

	fmt.Printf("A = %s\n", IntIntArrayToGridString(A))

	timeStart := time.Now()

	result := transpose(A)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToGridString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

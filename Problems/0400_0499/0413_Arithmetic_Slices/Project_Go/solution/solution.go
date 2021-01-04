package solution

import (
	"fmt"
	"strings"
	"time"
)

func numberOfArithmeticSlices(A []int) int {
	// 0ms
	li := make([]int, len(A))
	for i := 2; i < len(A); i++ {
		if A[i] - A[i - 1] == A[i - 1] - A[i - 2] {
			li[i] = li[i - 1] + 1
		}
	}

	res := 0
	for _, num := range(li) {
		res += num
	}

	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	A := StringToIntArray(flds)
	fmt.Printf("A = %s\n", IntArrayToString(A))

	timeStart := time.Now()

	result := numberOfArithmeticSlices(A)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

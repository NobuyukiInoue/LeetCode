package solution

import (
	"fmt"
	"strings"
	"time"
)

func minSwap(A []int, B []int) int {
	// 8ms
	swapRecord, fixRecord := 1, 0
	for i := 1; i < len(A); i++ {
		if A[i-1] >= B[i] || B[i-1] >= A[i] {
			swapRecord++
		} else if A[i-1] >= A[i] || B[i-1] >= B[i] {
			swapRecord, fixRecord = fixRecord+1, swapRecord
		} else {
			curMin := myMin(swapRecord, fixRecord)
			swapRecord = curMin + 1
			fixRecord = curMin
		}
	}
	return myMin(swapRecord, fixRecord)
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	A := StringToIntArray(flds[0])
	B := StringToIntArray(flds[1])
	fmt.Printf("A = [%s]\n", IntArrayToString(A))
	fmt.Printf("B = [%s]\n", IntArrayToString(B))

	timeStart := time.Now()

	result := minSwap(A, B)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

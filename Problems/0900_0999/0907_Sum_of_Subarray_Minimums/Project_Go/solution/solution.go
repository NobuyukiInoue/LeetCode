package solution

import (
	"fmt"
	"strings"
	"time"
)

const limit = 1000000007

func sumSubarrayMins(A []int) int {
	// 52ms
	var sol int
	mmap := make([]int, len(A))
	stack := []int{}
	for i := range A {
		var cur int
		for len(stack) != 0 && A[i] < A[stack[len(stack)-1]] {
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 {
			cur = (i + 1) * A[i]
		} else {
			cur = mmap[stack[len(stack)-1]] + (i-stack[len(stack)-1])*A[i]
		}
		cur %= limit
		stack = append(stack, i)
		mmap[i] = cur
		sol += cur
		sol %= limit
	}

	return sol
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	A := StringToIntArray(flds)
	fmt.Printf("A = [%s]\n", IntArrayToString(A))

	timeStart := time.Now()

	result := sumSubarrayMins(A)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

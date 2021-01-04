package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isIdealPermutation(A []int) bool {
	// 44ms
	for i := 0; i < len(A); i++ {
		if myAbs(A[i]-i) > 1 {
			return false
		}
	}
	return true
}

func myAbs(n int) int {
	if n >= 0 {
		return n
	}
	return -n
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

	result := isIdealPermutation(A)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

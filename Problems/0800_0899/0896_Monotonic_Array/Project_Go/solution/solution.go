package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isMonotonic(A []int) bool {
	for i := 0; i < len(A)-1; i++ {
		if A[i] == A[i+1] {
			continue
		}

		if A[i] > A[i+1] {
			return decreas(A)
		} else {
			break
		}
	}
	return increas(A)
}

func increas(A []int) bool {
	for i := 0; i < len(A)-1; i++ {
		if A[i] > A[i+1] {
			return false
		}
	}
	return true
}

func decreas(A []int) bool {
	for i := 0; i < len(A)-1; i++ {
		if A[i] < A[i+1] {
			return false
		}
	}
	return true
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

	result := isMonotonic(A)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

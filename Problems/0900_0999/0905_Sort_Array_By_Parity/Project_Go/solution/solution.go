package solution

import (
	"fmt"
	"strings"
	"time"
)

func sortArrayByParity(A []int) []int {
	for i, j := 0, 0; j < len(A); j++ {
		if A[j]%2 == 0 {
			tmp := A[i]
			A[i] = A[j]
			A[j] = tmp
			i++
		}
	}
	return A
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

	result := sortArrayByParity(A)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strings"
	"time"
)

func sortArrayByParityII(A []int) []int {
	// 320ms
	for i, j := 0, 1; i < len(A); i += 2 {
		if A[i]&1 == 0 {
			continue
		}
		for ; A[j]&1 != 0; j += 2 {
		}
		A[i], A[j] = A[j], A[i]
	}
	return A
}

func sortArrayByParityII_2(A []int) []int {
	// 308ms
	even, odd := 0, 1
	for true {
		for even < len(A) && A[even]%2 == 0 {
			even += 2
		}

		for odd < len(A) && A[odd]%2 != 0 {
			odd += 2
		}

		if odd >= len(A) || even >= len(A) {
			return A
		}

		temp := A[even]
		A[even] = A[odd]
		A[odd] = temp
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

	result := sortArrayByParityII(A)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

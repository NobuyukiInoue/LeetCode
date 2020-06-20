package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func largestSumAfterKNegations(A []int, K int) int {
	sort.Sort(sort.IntSlice(A))
	for i, j := 0, 0; i < K; i++ {
		if j+1 < len(A) && A[j+1] < A[j] {
			j++
		}
		A[j] = -A[j]
	}
	sum := 0
	for i := 0; i < len(A); i++ {
		sum += A[i]
	}
	return sum
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	A := StringToIntArray(flds[0])
	K, _ := strconv.Atoi(flds[1])

	fmt.Printf("A = [%s]\n", IntArrayToString(A))
	fmt.Printf("K = %d\n", K)

	timeStart := time.Now()

	result := largestSumAfterKNegations(A, K)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

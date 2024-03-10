package solution

import (
	"fmt"
	"strings"
	"time"
)

func findThePrefixCommonArray(A []int, B []int) []int {
	// 12ms - 22ms
	n := len(A)
	cnts := make([]int, n+1)
	C := make([]int, n)
	total := 0
	for i := 0; i < n; i++ {
		cnts[A[i]]++
		if cnts[A[i]] == 2 {
			total++
		}
		cnts[B[i]]++
		if cnts[B[i]] == 2 {
			total++
		}
		C[i] = total
	}
	return C
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	A, B := StringToIntArray(flds[0]), StringToIntArray(flds[1])
	fmt.Printf("A = [%s], B = [%s]\n", IntArrayToString(A), IntArrayToString(B))

	timeStart := time.Now()

	result := findThePrefixCommonArray(A, B)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

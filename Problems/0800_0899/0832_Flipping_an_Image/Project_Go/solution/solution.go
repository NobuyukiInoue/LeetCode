package solution

import (
	"fmt"
	"strings"
	"time"
)

func flipAndInvertImage(A [][]int) [][]int {
	n := len(A)
	for _, row := range A {
		for i := 0; i*2 < n; i++ {
			if row[i] == row[n-i-1] {
				row[n-i-1] = row[n-i-1] ^ 1
				row[i] = row[n-i-1]
			}
		}
	}
	return A
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

	result := flipAndInvertImage(A)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToGridString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", .Sub(timeStart).Seconds()*1000)
}

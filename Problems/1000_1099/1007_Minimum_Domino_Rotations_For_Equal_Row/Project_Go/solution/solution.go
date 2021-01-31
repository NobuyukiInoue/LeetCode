package solution

import (
	"fmt"
	"strings"
	"time"
)

func minDominoRotations(A []int, B []int) int {
	// 128ms
	countA, countB := getCount(A[0], A, B), getCount(B[0], A, B)
	if countA == -1 && countB == -1 {
		return -1
	}
	if countA == -1 {
		return countB
	}
	if countB == -1 {
		return countA
	}

	return myMin(countA, countB)
}

func getCount(x int, A []int, B []int) int {
	nA, nB := 0, 0
	for i := 0; i < len(A); i++ {
		if A[i] != x && B[i] != x {
			return -1
		}
		if A[i] != x {
			nA++
		}
		if B[i] != x {
			nB++
		}
	}
	return myMin(nA, nB)
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
	fmt.Printf("A = %s\n", IntArrayToString(A))
	fmt.Printf("B = %s\n", IntArrayToString(B))

	timeStart := time.Now()

	result := minDominoRotations(A, B)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strings"
	"time"
)

func computeArea(A int, B int, C int, D int, E int, F int, G int, H int) int {
	// 8ms
	areaOfSqrA := (C - A) * (D - B)
	areaOfSqrB := (G - E) * (H - F)
	left := myMax(A, E)
	right := myMin(G, C)
	bottom := myMax(F, B)
	top := myMin(D, H)
	overlap := 0
	if right > left && top > bottom {
		overlap = (right - left) * (top - bottom)
	}
	return areaOfSqrA + areaOfSqrB - overlap
}

func myMax(a int, b int) int {
	if a >= b {
		return a
	}
	return b
}

func myMin(a int, b int) int {
	if a <= b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	A, B, C, D, E, F, G, H := nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7]
	fmt.Printf("A = %d, B = %d, C = %d, D = %d, E = %d, F = %d, G = %d, H = %d\n", A, B, C, D, E, F, G, H)

	timeStart := time.Now()

	result := computeArea(A, B, C, D, E, F, G, H)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

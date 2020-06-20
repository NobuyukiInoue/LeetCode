package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxAbsValExpr(arr1 []int, arr2 []int) int {
	// 36ms
	res, n := 0, len(arr1)
	P := []int{-1, 1}

	for _, p := range P {
		for _, q := range P {
			closest := p*arr1[0] + q*arr2[0] + 0
			for i := 1; i < n; i++ {
				cur := p*arr1[i] + q*arr2[i] + i
				res = myMax(res, cur-closest)
				closest = myMin(closest, cur)
			}
		}
	}
	return res
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
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

	arr1 := StringToIntArray(flds[0])
	arr2 := StringToIntArray(flds[1])
	fmt.Printf("arr1 = [%s], arr2 = [%s]\n", IntArrayToString(arr1), IntArrayToString(arr2))

	timeStart := time.Now()

	result := maxAbsValExpr(arr1, arr2)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

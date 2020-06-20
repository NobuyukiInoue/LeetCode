package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findTheDistanceValue(arr1 []int, arr2 []int, d int) int {
	// 4ms
	res := 0
	for i := 0; i < len(arr1); i++ {
		for j := 0; j < len(arr2); j++ {
			if myAbs(arr1[i]-arr2[j]) <= d {
				break
			}

			if j == len(arr2)-1 {
				res++
			}
		}
	}
	return res
}

func myAbs(val int) int {
	if val >= 0 {
		return val
	}

	return -val
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
	d, _ := strconv.Atoi(flds[2])
	fmt.Printf("arr1 = [%s], arr2 = [%s], d = %d\n", IntArrayToString(arr1), IntArrayToString(arr2), d)

	timeStart := time.Now()

	result := findTheDistanceValue(arr1, arr2, d)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

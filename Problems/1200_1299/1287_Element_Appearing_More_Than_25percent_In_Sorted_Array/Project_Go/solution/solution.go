package solution

import (
	"fmt"
	"strings"
	"time"
)

func findSpecialInteger(arr []int) int {
	// 8ms
	n := len(arr)
	count := 1
	e := arr[0]
	for i := 1; i < n; i++ {
		if arr[i] == e {
			count++
		} else {
			e = arr[i]
			count = 1
		}
		if count > n/4 {
			return arr[i]
		}
	}
	return arr[0]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	arr := StringToIntArray(flds)
	fmt.Printf("arr = [%s]\n", IntArrayToString(arr))

	timeStart := time.Now()

	result := findSpecialInteger(arr)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

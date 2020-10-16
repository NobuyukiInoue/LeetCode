package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func containsPattern(arr []int, m int, k int) bool {
	// 0ms
	streak := 0
	for i := 0; i < len(arr) - m; i++ {
		if arr[i] == arr[i + m] {
			streak = streak + 1
		} else {
			streak = 0
		}

		if streak == (k - 1)*m {
			return true
		}
	}

	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	arr := StringToIntArray(flds[0])
	m, _ := strconv.Atoi(flds[1])
	k, _ := strconv.Atoi(flds[2])
	fmt.Printf("arr = [%s], m = %d, k = %d\n", IntArrayToString(arr), m, k)

	timeStart := time.Now()

	result := containsPattern(arr, m, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

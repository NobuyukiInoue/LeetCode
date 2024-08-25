package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxTurbulenceSize(arr []int) int {
	// 44ms - 46ms
	ans, clen := 0, 0
	for i := 0; i < len(arr); i++ {
		if i >= 2 && ((arr[i-2] > arr[i-1] && arr[i-1] < arr[i]) ||
			(arr[i-2] < arr[i-1] && arr[i-1] > arr[i])) {
			clen++
		} else if i >= 1 && arr[i-1] != arr[i] {
			clen = 2
		} else {
			clen = 1
		}
		ans = myMax(ans, clen)
	}
	return ans
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	arr := StringToIntArray(flds)
	fmt.Printf("arr = [%s]\n", IntArrayToString(arr))

	timeStart := time.Now()

	result := maxTurbulenceSize(arr)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

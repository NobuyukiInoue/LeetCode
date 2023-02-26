package solution

import (
	"fmt"
	"strings"
	"time"
)

func hIndex(citations []int) int {
	// 12ms
	n := len(citations)
	low, high := 0, n
	for low < high {
		mid := (low + high) / 2
		k := n - mid
		if k > citations[mid] {
			low = mid + 1
		} else if mid == 0 || k < citations[mid-1] {
			high = mid
		} else {
			return k
		}
	}
	return n - low
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	citations := StringToIntArray(flds)
	fmt.Printf("citations = [%s]\n", IntArrayToString(citations))

	timeStart := time.Now()

	result := hIndex(citations)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

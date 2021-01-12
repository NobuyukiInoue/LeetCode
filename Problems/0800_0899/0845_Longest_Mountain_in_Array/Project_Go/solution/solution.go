package solution

import (
	"fmt"
	"strings"
	"time"
)

func longestMountain(arr []int) int {
	// 16ms
	if len(arr) < 3 {
		return 0
	}

	largestMountain := 0
	start, end := 0, 0
	arrLength := len(arr)
	for end < arrLength {
		start = end
		if end + 1 < arrLength && arr[end] < arr[end + 1] {
			for end + 1 < arrLength && arr[end] < arr[end + 1] {
				end++
			}
			if end + 1 < arrLength && arr[end] > arr[end + 1] {
				for (end + 1) < arrLength && arr[end] > arr[end + 1] {
					end++
				}
				largestMountain = myMax(largestMountain, end - start + 1)
			}
		}
		if end == start {
			end++
		}
	}
	return largestMountain
}

func myMax(a int, b int) int {
	if a > b {
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

	arr := StringToIntArray(flds)
	fmt.Printf("arr = %s\n", IntArrayToString(arr))

	timeStart := time.Now()

	result := longestMountain(arr)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

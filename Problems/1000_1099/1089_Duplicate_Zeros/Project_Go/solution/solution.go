package solution

import (
	"fmt"
	"strings"
	"time"
)

func duplicateZeros(arr []int) {
	// 32ms
	helper(arr, 0)
}

func helper(arr []int, cnt int) {
	if len(arr) <= cnt {
		return
	}
	i := 0
	for i = 0; i < len(arr); i++ {
		if arr[i] == 0 {
			break
		}
	}
	if i != len(arr) {
		helper(arr[i+1:], cnt+1)
	}
	if i+cnt+1 < len(arr) {
		arr[i+cnt+1] = 0
	}
	for j := min(i, len(arr)-cnt-1); j >= 0; j-- {
		arr[j+cnt] = arr[j]
	}
}

func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func duplicateZeros2(arr []int) {
	// 44ms
	countZero := 0
	for i := 0; i < len(arr); i++ {
		if arr[i] == 0 {
			countZero++
		}
	}
	arrLen := len(arr) + countZero
	for i, j := len(arr)-1, arrLen-1; i < j; i-- {
		if arr[i] != 0 {
			if j < len(arr) {
				arr[j] = arr[i]
			}
		} else {
			if j < len(arr) {
				arr[j] = arr[i]
			}
			j--
			if j < len(arr) {
				arr[j] = arr[i]
			}
		}
		j--
	}
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

	duplicateZeros(arr)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(arr))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

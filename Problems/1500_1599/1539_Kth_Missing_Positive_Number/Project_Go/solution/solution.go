package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findKthPositive(arr []int, k int) int {
	// 4ms
	count, index := 0, 0
	arrLength := len(arr)
	for i := 1; i < arr[arrLength-1]; i++ {
		if i < arr[index] {
			count++
			if count == k {
				return i
			}
		} else {
			index++
		}
	}
	return arr[arrLength-1] + k - count
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	arr := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("arr = [%s], k = %d\n", IntArrayToString(arr), k)

	timeStart := time.Now()

	result := findKthPositive(arr, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"math"
	"sort"
	"strings"
	"time"
)

func minimumAbsDifference(arr []int) [][]int {
	min := math.MaxInt32
	res := [][]int{}

	sort.Slice(arr, func(i, j int) bool {
		return arr[i] < arr[j]
	})

	for i := 1; i < len(arr); i++ {
		if arr[i]-arr[i-1] < min {
			min = arr[i] - arr[i-1]
		}
		if min == 1 {
			break
		}
	}
	for i := 1; i < len(arr); i++ {
		if arr[i]-arr[i-1] == min {
			res = append(res, []int{arr[i-1], arr[i]})
		}
	}
	return res
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

	result := minimumAbsDifference(arr)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

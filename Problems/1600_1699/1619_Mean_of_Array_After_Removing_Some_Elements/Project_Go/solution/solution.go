package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func trimMean(arr []int) float64 {
	// 8ms
	n := len(arr)
	total := float64(0.0)
	sort.Sort(sort.IntSlice(arr))
	var i int
	for i = n/20; i < n - n/20; i++ {
		total += float64(arr[i])
	}
	return total/(float64(n)*9/10)
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

	result := trimMean(arr)

	timeEnd := time.Now()

	fmt.Printf("result = %f\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

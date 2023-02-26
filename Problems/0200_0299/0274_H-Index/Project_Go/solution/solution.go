package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func hIndex(citations []int) int {
	// 0ms - 3ms
	sort.Sort(sort.IntSlice(citations))
	n := len(citations)
	i := 0
	for i < n && n-i > citations[i] {
		i++
	}
	return n - i
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

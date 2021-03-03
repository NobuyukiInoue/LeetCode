package solution

import (
	"fmt"
	"math"
	"sort"
	"strings"
	"time"
)

func minIncrementForUnique(A []int) int {
	// 64ms
	sort.Sort(sort.IntSlice(A))
	last := math.MinInt64
	res := 0
	for _, a := range(A) {
		if a <= last {
			last++
			res += last - a
		} else {
			last = a
	   }
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	A := StringToIntArray(flds)
	fmt.Printf("A = %s\n", IntArrayToString(A))

	timeStart := time.Now()

	result := minIncrementForUnique(A)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

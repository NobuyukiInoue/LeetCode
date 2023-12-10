package solution

import (
	"fmt"
	"strings"
	"time"
)

func findPeaks(mountain []int) []int {
	// 6ms
	var res []int
	for i := 1; i < len(mountain)-1; i++ {
		if mountain[i-1] < mountain[i] && mountain[i] > mountain[i+1] {
			res = append(res, i)
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	mountain := StringToIntArray(flds)
	fmt.Printf("mountain = [%s]\n", IntArrayToString(mountain))

	timeStart := time.Now()

	result := findPeaks(mountain)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

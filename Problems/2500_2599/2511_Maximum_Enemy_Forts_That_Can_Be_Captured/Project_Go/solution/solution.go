package solution

import (
	"fmt"
	"strings"
	"time"
)

func captureForts(forts []int) int {
	// 2ms
	current_idx, max_forts := 0, 0
	for i, fort := range forts {
		if fort != 0 {
			if forts[current_idx] == -fort {
				max_forts = myMax(max_forts, i-current_idx-1)
			}
			current_idx = i
		}
	}
	return max_forts
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

	forts := StringToIntArray(flds)
	fmt.Printf("forts = [%s]\n", IntArrayToString(forts))

	timeStart := time.Now()

	result := captureForts(forts)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strings"
	"time"
)

func largestAltitude(gain []int) int {
	// 0ms
	height, heightMax := 0, 0
	for _, v := range(gain) {
		height += v
		if height > heightMax {
			heightMax = height
		}
	}
	return heightMax
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	gain := StringToIntArray(flds)
	fmt.Printf("gain = %s\n", IntArrayToString(gain))

	timeStart := time.Now()

	result := largestAltitude(gain)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

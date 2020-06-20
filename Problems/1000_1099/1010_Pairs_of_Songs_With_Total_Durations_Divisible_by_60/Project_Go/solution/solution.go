package solution

import (
	"fmt"
	"strings"
	"time"
)

func numPairsDivisibleBy60(time []int) int {
	freq := make([]int, 60)
	for _, dur := range time {
		freq[dur%60]++
	}

	res := 0
	for i := 1; i < 30; i++ {
		res += freq[i] * freq[60-i]
	}

	res += freq[0] * (freq[0] - 1) / 2
	res += freq[30] * (freq[30] - 1) / 2

	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	vartime := StringToIntArray(flds)
	fmt.Printf("time = [%s]\n", IntArrayToString(vartime))

	timeStart := time.Now()

	result := numPairsDivisibleBy60(vartime)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

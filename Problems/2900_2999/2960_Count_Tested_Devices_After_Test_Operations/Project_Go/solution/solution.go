package solution

import (
	"fmt"
	"strings"
	"time"
)

func countTestedDevices(batteryPercentages []int) int {
	// 0ms
	ans := 0
	for _, target := range batteryPercentages {
		if target > ans {
			ans++
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	batteryPercentages := StringToIntArray(flds)
	fmt.Printf("batteryPercentages = [%s]\n", IntArrayToString(batteryPercentages))

	timeStart := time.Now()

	result := countTestedDevices(batteryPercentages)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

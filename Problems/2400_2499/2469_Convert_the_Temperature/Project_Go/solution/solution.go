package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func convertTemperature(celsius float64) []float64 {
	// 1ms - 3ms
	return []float64{celsius + 273.15, celsius*1.80 + 32.00}
}

func dbleArrayToString(nums []float64) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.FormatFloat(nums[0], 'f', 2, 64)
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.FormatFloat(nums[i], 'f', 2, 64)
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	celsius, _ := strconv.ParseFloat(flds, 64)
	fmt.Printf("celsius = %f\n", celsius)

	timeStart := time.Now()

	result := convertTemperature(celsius)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", dbleArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

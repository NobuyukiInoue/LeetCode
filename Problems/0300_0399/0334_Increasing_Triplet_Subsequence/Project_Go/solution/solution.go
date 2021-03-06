package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func increasingTriplet(nums []int) bool {
	// 4ms
	first := math.MaxInt64
	second := math.MaxInt64
	for _, n := range nums {
		if n <= first {
			first = n
		} else if n <= second {
			second = n
		} else {
			return true
		}
	}
	return false
}

func strArrayToString(data []string) string {
	if len(data) <= 0 {
		return ""
	}

	resultStr := data[0]
	for i := 1; i < len(data); i++ {
		resultStr += ", " + data[i]
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := increasingTriplet(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

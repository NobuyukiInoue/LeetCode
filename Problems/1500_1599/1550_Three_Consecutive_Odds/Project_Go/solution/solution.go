package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func threeConsecutiveOdds(arr []int) bool {
	// 0ms
	i := 0
	for i < len(arr) - 2 {
		if arr[i] % 2 == 0 {
			i++
			continue
		}
		i++
		if arr[i] % 2 == 0 {
			continue
		}
		i++
		if arr[i] % 2 == 0 {
			continue
		}
		return true
	}
	return false
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

	result := threeConsecutiveOdds(arr)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

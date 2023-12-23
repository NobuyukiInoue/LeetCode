package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func canReach(arr []int, start int) bool {
	// 24ms - 33ms
	if start < 0 || start >= len(arr) || arr[start] < 0 {
		return false
	}
	arr[start] *= -1
	return arr[start] == 0 || canReach(arr, start+arr[start]) || canReach(arr, start-arr[start])
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	arr := StringToIntArray(flds[0])
	start, _ := strconv.Atoi(flds[1])
	fmt.Printf("arr = [%s], start = %d\n", IntArrayToString(arr), start)

	timeStart := time.Now()

	result := canReach(arr, start)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

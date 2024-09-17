package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func sampleStats(count []int) []float64 {
	// 2ms
	v_min, v_max := -1, -1
	n := 0
	v_sum := int64(0)
	v_maxcnt, mode := 0, 0
	for i, cur := range count {
		if cur == 0 {
			continue
		}
		if v_min == -1 {
			v_min = i
		}
		v_max = myMax(v_max, i)
		n += cur
		v_sum += int64(i) * int64(cur)
		if cur > v_maxcnt {
			v_maxcnt = cur
			mode = i
		}
	}
	var median float64
	if n%2 == 1 {
		median = float64(kth(count, n/2+1))
	} else {
		median = float64(kth(count, n/2)+kth(count, n/2+1)) / 2.0
	}
	return []float64{float64(v_min), float64(v_max), float64(v_sum) / float64(n), median, float64(mode)}
}

func kth(count []int, k int) int {
	for i, cur := range count {
		k -= cur
		if k <= 0 {
			return i
		}
	}
	return 0
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func Float64ArrayToString(nums []float64) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.FormatFloat(nums[0], 'f', 5, 64)
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.FormatFloat(nums[i], 'f', 5, 64)
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	count := StringToIntArray(flds)
	fmt.Printf("count = [%s]\n", IntArrayToString(count))

	timeStart := time.Now()

	result := sampleStats(count)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", Float64ArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

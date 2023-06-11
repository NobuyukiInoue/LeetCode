package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func kthSmallestPrimeFraction(arr []int, k int) []int {
	// 5ms
	lo, hi := 0.0, 1.0
	for lo < hi {
		mid := (lo + hi) / 2.0
		count := 0
		best := []int{0, 1}
		left := 0
		for right := 1; right < len(arr); right++ {
			for float64(arr[left]) < mid*float64(arr[right]) {
				left++
			}
			count += left
			if left > 0 && best[0]*arr[right] < best[1]*arr[left-1] {
				best = []int{arr[left-1], arr[right]}
			}
		}
		if count == k {
			return best
		} else if count > k {
			hi = mid
		} else {
			lo = mid
		}
	}
	return []int{0, 0}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	arr := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("arr = [%s], k = %d\n", IntArrayToString(arr), k)

	timeStart := time.Now()

	result := kthSmallestPrimeFraction(arr, k)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

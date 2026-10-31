package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func findValidElements(nums []int) []int {
	// 0ms
	numsL := []int{0}
	numsR := []int{math.MaxInt}
	for _, num := range nums {
		for len(numsR) > 0 && num >= numsR[len(numsR)-1] {
			numsR = numsR[:len(numsR)-1]
		}
		if num > numsL[len(numsL)-1] {
			numsL = append(numsL, num)
		} else {
			numsR = append(numsR, num)
		}
	}
	ans := append([]int{}, numsL[1:]...)
	ans = append(ans, numsR[1:]...)
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := findValidElements(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

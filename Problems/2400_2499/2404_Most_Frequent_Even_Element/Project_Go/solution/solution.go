package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func mostFrequentEven(nums []int) int {
	// 41ms - 91ms
	var ans = -1
	var ansFreq int
	var count = make(map[int]int)
	for _, num := range nums {
		if num%2 == 0 {
			count[num]++
		}
	}
	for num, freq := range count {
		if freq > ansFreq || (freq == ansFreq && num < ans) {
			ansFreq = freq
			ans = num
		}
	}
	return ans
}

func mostFrequentEven2(nums []int) int {
	// 99ms - 143ms
	cnts := make(map[int]int, 0)
	ans, max_cnts := math.MaxInt, 0
	for _, num := range nums {
		if num%2 == 0 {
			cnts[num]++
			if cnts[num] == max_cnts {
				ans = myMin(ans, num)
			}
			if cnts[num] > max_cnts {
				max_cnts = cnts[num]
				ans = num
			}
		}
	}
	if len(cnts) == 0 {
		return -1
	}
	return ans
}

func myMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := mostFrequentEven(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

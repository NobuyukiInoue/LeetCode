package solution

import (
	"fmt"
	"math"
	"sort"
	"strings"
	"time"
)

func longestSquareStreak(nums []int) int {
	// 198ms - 204ms
	sort.Sort(sort.IntSlice(nums))
	var ans int = 1
	Map := make(map[int]int)
	for _, num := range nums {
		sqrtNum := int(math.Sqrt(float64(num)))
		if sqrtNum*sqrtNum == num {
			Map[num] = Map[sqrtNum] + 1
			if Map[num] > ans {
				ans = Map[num]
			}
		} else {
			Map[num] = 1
		}
	}
	if ans == 1 {
		return -1
	}
	return ans
}

func longestSquareStreak2(nums []int) int {
	// 211ms - 214ms
	sort.Sort(sort.Reverse(sort.IntSlice(nums)))
	seen := make(map[int]int)
	ans := -1
	for _, num := range nums {
		_, ok := seen[num*num]
		if ok {
			seen[num] = seen[num*num] + 1
			ans = int(math.Max(float64(ans), float64(seen[num])))
		} else {
			seen[num] = 1
		}

	}
	return ans
}

func longestSquareStreak3(nums []int) int {
	// Time Limit Exceeded.
	max := 0
	for _, num := range nums {
		cnt, l_num := 1, num
		for Contains(nums, l_num*l_num) {
			l_num = l_num * l_num
			cnt++
		}
		max = myMax(max, cnt)
	}
	if max == 1 {
		return -1
	}
	return max
}

func Contains(nums []int, target int) bool {
	for _, num := range nums {
		if num == target {
			return true
		}
	}
	return false
}

func myMax(a, b int) int {
	if a > b {
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

	result := longestSquareStreak(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

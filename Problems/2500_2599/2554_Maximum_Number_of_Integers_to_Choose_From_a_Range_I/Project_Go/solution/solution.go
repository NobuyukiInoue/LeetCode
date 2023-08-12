package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func maxCount(banned []int, n int, maxSum int) int {
	// 213ms - 225ms
	set := make(map[int]bool, 0)
	for _, ban := range banned {
		set[ban] = true
	}
	ans, total := 0, 0
	for i := 1; i < n+1; i++ {
		if total+i > maxSum {
			break
		}
		if _, ok := set[i]; !ok {
			total += i
			ans++
		}
	}
	return ans
}

func maxCount2(banned []int, n int, maxSum int) int {
	// 744ms - 856ms
	ans, total := 0, 0
	for i := 1; i < n+1; i++ {
		if total+i > maxSum {
			break
		}
		if !contains(banned, i) {
			total += i
			ans++
		}
	}
	return ans
}

func contains(nums []int, target int) bool {
	for _, num := range nums {
		if num == target {
			return true
		}
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	banned := StringToIntArray(flds[0])
	n, _ := strconv.Atoi(flds[1])
	maxSum, _ := strconv.Atoi(flds[2])
	fmt.Printf("banned = [%s], n = %d, maxSum = %d\n", IntArrayToString(banned), n, maxSum)

	timeStart := time.Now()

	result := maxCount(banned, n, maxSum)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

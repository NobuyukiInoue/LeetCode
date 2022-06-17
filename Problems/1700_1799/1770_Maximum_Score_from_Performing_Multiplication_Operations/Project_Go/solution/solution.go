package solution

import (
	"fmt"
	"strings"
	"time"
)

func maximumScore(nums []int, multipliers []int) int {
	// 149ms - 213ms
	n, m := len(nums), len(multipliers)
	first, second := make([]int, n), make([]int, n)
	for i := 0; i < n; i++ {
		if n-1 < m {
			first[i] = nums[i] * multipliers[(n-1)]
		} else {
			first[i] = 0
		}
	}
	for l := 2; l <= n; l++ {
		for i := 0; i+l-1 < n && (n-l < m); i++ {
			j := i + l - 1
			if n-l < m {
				second[i] = myMax(first[i+1]+multipliers[n-l]*nums[i], first[i]+multipliers[n-l]*nums[j])
			} else {
				second[i] = myMax(first[i+1], first[i])
			}
		}
		first = second
	}
	return first[0]
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_mat := strings.Split(flds, "],[")
	arr := make([][]int, len(str_mat))
	for i := 0; i < len(str_mat); i++ {
		arr[i] = StringToIntArray(str_mat[i])
	}
	nums, multipliers := arr[0], arr[1]
	fmt.Printf("nums = [%s], multipliers = [%s]\n", IntArrayToString(nums), IntArrayToString(multipliers))

	timeStart := time.Now()

	result := maximumScore(nums, multipliers)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

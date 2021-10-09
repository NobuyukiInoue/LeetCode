package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func nextGreaterElement(n int) int {
	// 0ms
	s := getDigitsArray(n)
	i := len(s) - 1
	for i-1 >= 0 && s[i] <= s[i-1] {
		i--
	}
	if i == 0 {
		return -1
	}
	j := i
	for j+1 < len(s) && s[j+1] > s[i-1] {
		j++
	}

	swap(s, i-1, j)
	reversed(s, i)

	ans := int64(0)
	for i = 0; i < len(s); i++ {
		ans *= 10
		ans += int64(s[i])
	}
	if ans <= ((1 << 31) - 1) {
		return int(ans)
	}
	return -1
}

func getDigitsArray(n int) []int {
	nums := make([]int, 0)
	for temp_n := n; temp_n > 0; temp_n /= 10 {
		nums = append(nums, temp_n%10)
	}
	reversed(nums, 0)
	return nums
}

func swap(nums []int, i int, j int) {
	nums[i], nums[j] = nums[j], nums[i]
}

func reversed(nums []int, start_pos int) {
	n := len(nums)
	for k := start_pos; k < n-(n-start_pos)/2; k++ {
		swap(nums, k, n+start_pos-k-1)
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	n, _ := strconv.Atoi(flds)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := nextGreaterElement(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

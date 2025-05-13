package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxLength(nums []int) int {
	// 0ms - 3ms
	n, ans := len(nums), 2
	var i, j int
	for i = 0; i < n-1; i++ {
		v_gcd, v_lcm := nums[i], nums[i]
		is_longest := false
		for j = i + 1; j < n; j++ {
			v_gcd = gcd(v_gcd, nums[j])
			if v_gcd != 1 || gcd(v_lcm, nums[j]) != 1 {
				ans = myMax(ans, j-i)
				is_longest = true
				break
			}
			v_lcm *= nums[j]
		}
		if !is_longest {
			ans = myMax(ans, j-i)
		}
	}
	return ans
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := maxLength(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

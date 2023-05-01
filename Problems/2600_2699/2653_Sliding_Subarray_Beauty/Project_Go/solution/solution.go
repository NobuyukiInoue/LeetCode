package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func getSubarrayBeauty(nums []int, k int, x int) []int {
	// 292ms - 320ms
	n := len(nums)
	freq := make([]int, 51)
	ans := make([]int, n-k+1)
	j, idx := 0, 0
	for i := 0; i < n; i++ {
		if nums[i] < 0 {
			freq[myAbs(nums[i])]++
		}
		if i-j+1 >= k {
			cnt := 0
			for L := 50; L > 0; L-- {
				cnt += freq[L]
				if cnt >= x {
					ans[idx] = -L
					idx++
					break
				}
			}
			if cnt < x {
				ans[idx] = 0
				idx++
			}
			if nums[j] < 0 {
				freq[myAbs(nums[j])]--
			}
			j++
		}
	}
	return ans
}

func myAbs(n int) int {
	if n >= 0 {
		return n
	}
	return -n
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	x, _ := strconv.Atoi(flds[2])
	fmt.Printf("nums = [%s], k = %d, x = %d\n", IntArrayToString(nums), k, x)

	timeStart := time.Now()

	result := getSubarrayBeauty(nums, k, x)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

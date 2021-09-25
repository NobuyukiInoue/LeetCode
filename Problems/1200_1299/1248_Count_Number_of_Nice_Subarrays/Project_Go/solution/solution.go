package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func numberOfSubarrays(nums []int, k int) int {
	// 112ms
	magic := make([]int, 0)
	evenCount := 0
	for _, v := range nums {
		if v%2 == 0 {
			evenCount++
		} else {
			magic = append(magic, evenCount+1)
			evenCount = 0
		}
	}
	magic = append(magic, evenCount+1)
	subArrays := 0
	for i := k; i < len(magic); i++ {
		subArrays += magic[i-k] * magic[i]
	}
	return subArrays
}

func numberOfSubarrays2(nums []int, k int) int {
	// 164ms
	left, right := make(map[int]int), make(map[int]int)
	i, n, cnt := 0, 0, 0
	for i < len(nums) {
		if nums[i]%2 == 0 {
			cnt++
			i++
		} else {
			left[n], right[n-1] = cnt, cnt
			cnt = 0
			i++
			n++
		}
	}
	right[n-1] = cnt
	res := 0
	for i := 0; i+k-1 <= n-1; i++ {
		res += (1 + left[i]) * (1 + right[i+k-1])
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	nums := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = %s, k = %d\n", IntArrayToString(nums), k)

	timeStart := time.Now()

	result := numberOfSubarrays(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

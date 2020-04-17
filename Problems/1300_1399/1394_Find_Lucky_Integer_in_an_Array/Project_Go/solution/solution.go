package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findLucky(arr []int) int {
	// 4ms
	freq := make(map[int]int, 0)
	for _, v := range arr {
		value, exists := freq[v]
		if exists {
			freq[v] = value + 1
		} else {
			freq[v] = 1
		}
	}

	ans := -1
	for k, v := range freq {
		if k == v {
			ans = myMax(ans, k)
		}
	}
	return ans
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func strToIntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intArrayToString(nums []int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	arr := strToIntArray(flds)
	fmt.Printf("arr = [%s]\n", intArrayToString(arr))

	timeStart := time.Now()

	result := findLucky(arr)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

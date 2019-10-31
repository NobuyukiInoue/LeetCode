package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func subsetsWithDup(nums []int) [][]int {
	// 4ms
	res := [][]int{}
	sort.Ints(nums)

	var dfs func(int, []int)
	dfs = func(index int, temp []int) {
		res = append(res, temp)
		n := len(temp) + 1
		for i := index; i < len(nums); i++ {
			if i == index || nums[i] != nums[i-1] {
				dfs(i+1, append(temp, nums[i])[:n:n])
			}
		}
	}

	temp := make([]int, 0, 0)
	dfs(0, temp)

	return res
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
	nums := strToIntArray(flds)

	fmt.Printf("nums = %s\n", intArrayToString(nums))
	timeStart := time.Now()

	result := subsetsWithDup(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [")
	for i := 0; i < len(result); i++ {
		if i == 0 {
			fmt.Printf("[%s]", intArrayToString(result[i]))
		} else {
			fmt.Printf(",[%s]", intArrayToString(result[i]))
		}
	}
	fmt.Printf("]\n")
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

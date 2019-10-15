package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func combinationSum(candidates []int, target int) [][]int {
	// 0ms
	result := make([][]int, 0)

	sort.Ints(candidates)
	dfs(candidates, target, []int{}, &result)

	return result
}

func dfs(candidates []int, target int, current []int, result *[][]int) {
	for i, v := range candidates {
		if target-v <= 0 {
			if target-v == 0 {
				match := make([]int, len(current)+1)
				copy(match, current)
				match[len(current)] = v
				*result = append(*result, match)
			}
			break
		}

		dfs(candidates[i:], target-v, append(current, v), result)
	}
}

func str2IntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func printIntArray(nums []int) string {
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
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	candidates := str2IntArray(flds[0])
	target, _ := strconv.Atoi(flds[1])

	fmt.Printf("candidates = %s, target = %d\n", printIntArray(candidates), target)

	timeStart := time.Now()

	result := combinationSum(candidates, target)

	timeEnd := time.Now()

	fmt.Printf("result = ")
	for i := 0; i < len(result); i++ {
		if i == 0 {
			fmt.Printf("[%s]", printIntArray(result[i]))
		} else {
			fmt.Printf(",[%s]", printIntArray(result[i]))
		}
	}
	fmt.Printf("]\n")

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

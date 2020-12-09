package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func canPartitionKSubsets(nums []int, k int) bool {
	// 0ms
	total := 0
	for _, num := range nums {
		total += num
	}
	if k <= 0 || total%k != 0 {
		return false
	}
	visited := make([]bool, len(nums))
	return dfs(nums, visited, 0, k, 0, total/k)
}

func dfs(nums []int, visited []bool, startIndex int, k int, currentSum int, target int) bool {
	if k == 1 {
		return true
	}
	if currentSum > target {
		return false
	}
	if currentSum == target {
		return dfs(nums, visited, 0, k-1, 0, target)
	}
	for i := startIndex; i < len(nums); i++ {
		if !visited[i] {
			visited[i] = true
			if dfs(nums, visited, i+1, k, currentSum+nums[i], target) {
				return true
			}
			visited[i] = false
		}
	}
	return false
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
	fmt.Printf("nums = [%s], k = %d\n", IntArrayToString(nums), k)

	timeStart := time.Now()

	result := canPartitionKSubsets(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

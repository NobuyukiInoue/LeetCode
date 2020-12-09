package solution

import (
	"fmt"
	"strings"
	"time"
)

var ans [][]int
var nums2 []int
var numslen int

func findSubsequences(nums []int) [][]int {
	// 52ms
	ans = make([][]int, 0)
	nums2 = nums
	numslen = len(nums)
	dfs(-1, []int{})
	return ans
}

func dfs(i int, curr []int) {
	if len(curr) > 1 {
		ans = append(ans, curr)
	}
	found := make([]int, 0)
	for j := i + 1; j < numslen; j++ {
		if (i >= 0 && nums2[j] < nums2[i]) || contains(found, nums2[j]) {
			continue
		}
		currCopy := append([]int{}, curr...)
		currCopy = append(currCopy, nums2[j])
		dfs(j, currCopy)
		found = append(found, nums2[j])
	}
}

func contains(nums []int, target int) bool {
	for _, n := range nums {
		if n == target {
			return true
		}
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := findSubsequences(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

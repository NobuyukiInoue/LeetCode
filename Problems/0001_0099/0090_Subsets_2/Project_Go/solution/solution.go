package solution

import (
	"fmt"
	"sort"
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

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	nums := StringToIntArray(flds)

	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := subsetsWithDup(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

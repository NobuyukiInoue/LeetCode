package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func lastStoneWeight(stones []int) int {
	for len(stones) > 1 {
		sort.Ints(stones)
		diff := stones[len(stones)-1] - stones[len(stones)-2]
		stones = stones[:len(stones)-2]
		stones = append(stones, diff)
	}
	return stones[0]
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
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	stones := make([]int, len(flds))
	for i := 0; i < len(flds); i++ {
		stones[i], _ = strconv.Atoi(flds[i])
	}

	fmt.Printf("stones = %s\n", printIntArray(stones))
	timeStart := time.Now()

	result := lastStoneWeight(stones)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

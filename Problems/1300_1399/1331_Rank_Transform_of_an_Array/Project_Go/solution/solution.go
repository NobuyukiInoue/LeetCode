package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func arrayRankTransform(arr []int) []int {
	// Time Limit Exceeded
	if len(arr) <= 0 {
		return arr
	}

	sorted_arr := make([]int, len(arr))
	copy(sorted_arr[:], arr[:])
	sort.Sort(sort.IntSlice(sorted_arr))

	mp := make(map[int]int)
	rank := 1
	mp[sorted_arr[0]] = rank
	for i := 1; i < len(sorted_arr); i++ {
		if sorted_arr[i-1] != sorted_arr[i] {
			rank++
		}
		mp[sorted_arr[i]] = rank
	}

	ranks := make([]int, len(arr))
	for i := 0; i < len(arr); i++ {
		ranks[i] = mp[arr[i]]
	}

	return ranks
}

func str2IntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intintArrayToString(nums [][]int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := "[" + intArrayToString(nums[0]) + "]"
	for i := 1; i < len(nums); i++ {
		resultStr += ", [" + intArrayToString(nums[i]) + "]"
	}

	return resultStr
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

	arr := str2IntArray(flds)
	fmt.Printf("arr = [%s]\n", intArrayToString(arr))

	timeStart := time.Now()

	result := arrayRankTransform(arr)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", intArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

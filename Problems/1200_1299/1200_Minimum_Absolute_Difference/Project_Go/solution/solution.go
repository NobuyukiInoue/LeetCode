package solution

import (
	"fmt"
	"math"
	"sort"
	"strconv"
	"strings"
	"time"
)

func minimumAbsDifference(arr []int) [][]int {
	min := math.MaxInt32
	res := [][]int{}

	sort.Slice(arr, func(i, j int) bool {
		return arr[i] < arr[j]
	})

	for i := 1; i < len(arr); i++ {
		if arr[i]-arr[i-1] < min {
			min = arr[i] - arr[i-1]
		}
		if min == 1 {
			break
		}
	}
	for i := 1; i < len(arr); i++ {
		if arr[i]-arr[i-1] == min {
			res = append(res, []int{arr[i-1], arr[i]})
		}
	}
	return res
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

	result := minimumAbsDifference(arr)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", intintArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func sortByBits(arr []int) []int {
	// 4ms
	sort.Sort(sort.IntSlice(arr))

	arrLength := len(arr)
	maxBits, temp := 0, arr[arrLength-1]

	for temp > 0 {
		temp >>= 1
		maxBits += 1
	}
	table := make([][]int, maxBits)
	for i := 0; i < maxBits; i++ {
		table[i] = make([]int, 0)
	}

	for i := 0; i < arrLength; i++ {
		table[countBits(arr[i])] = append(table[countBits(arr[i])], arr[i])
	}

	res := make([]int, 0)
	for i := 0; i < len(table); i++ {
		if len(table[i]) > 0 {
			res = append(res, table[i]...)
		}
	}

	return res
}

func sortByBits2(arr []int) []int {
	// 8ms
	sort.Slice(arr, func(i, j int) bool {
		iCount, jCount := countBits(arr[i]), countBits(arr[j])
		if iCount == jCount {
			return arr[i] < arr[j]
		}
		return iCount < jCount
	})
	return arr
}

func countBits(num int) int {
	count := 0
	for ; num > 0; num >>= 1 {
		if num%2 == 1 {
			count++
		}
	}
	return count
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

	result := sortByBits(arr)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", intArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

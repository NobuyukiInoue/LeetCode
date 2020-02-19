package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func containsNearbyAlmostDuplicate(nums []int, k int, t int) bool {
	// 0ms
	n := len(nums)
	indexs := make([]int, n)
	for i := 0; i < n; i++ {
		indexs[i] = i
	}

	quicksort(nums, indexs, 0, n-1)

	for i := 0; i < n; i++ {
		start := nums[i]
		sindex := indexs[i]
		for j := i + 1; j < n; j++ {
			end := nums[j]
			eindex := indexs[j]
			diff := end - start
			if diff > t {
				break
			}
			if myAbs(eindex-sindex) <= k {
				return true
			}
		}
	}
	return false
}

func myAbs(a int) int {
	if a >= 0 {
		return a
	}

	return -a
}

func quicksort(nums []int, indexs []int, start int, end int) {
	if start >= end {
		return
	}

	mid := start + (end-start)/2
	pivot := nums[mid]
	i, j := start, end
	for i <= j {
		for nums[i] < pivot {
			i++
		}
		for nums[j] > pivot {
			j--
		}
		if i <= j {
			if nums[i] != nums[j] {
				swap(nums, indexs, i, j)
			}
			i++
			j--
		}
	}
	quicksort(nums, indexs, start, i-1)
	quicksort(nums, indexs, i, end)
}

func swap(nums []int, indexs []int, i int, j int) {
	value := nums[i]
	nums[i] = nums[j]
	nums[j] = value
	index := indexs[i]
	indexs[i] = indexs[j]
	indexs[j] = index
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
	temp = strings.Replace(temp, "[[", "", -1)

	flds := strings.Split(temp, "],")

	data := strings.Split(flds[0], ",")
	nums := make([]int, len(data))
	for i := 0; i < len(data); i++ {
		nums[i], _ = strconv.Atoi(data[i])
	}

	fld1 := strings.Split(strings.Replace(flds[1], "]", "", -1), ",")
	k, _ := strconv.Atoi(fld1[0])
	t, _ := strconv.Atoi(fld1[1])

	fmt.Printf("nums = [%s]\n", intArrayToString(nums))
	fmt.Printf("k = %d, t = %d\n", k, t)

	timeStart := time.Now()

	result := containsNearbyAlmostDuplicate(nums, k, t)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

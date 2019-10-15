package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func containsNearbyDuplicate(nums []int, k int) bool {
	m := make(map[int]int, len(nums))
	for i, val := range nums {
		v, ok := m[val]
		if ok {
			if int(i-v) <= k {
				return true
			}
		}
		m[val] = i
	}
	return false
}

func containsNearbyDuplicate2(nums []int, k int) bool {
	nums2 := removeDuplicate1(nums)
	if len(nums) == len(nums2) {
		return false
	}

	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if j-i > k {
				break
			}
			if nums[i] == nums[j] {
				return true
			}
		}
	}

	return false
}

// 重複した要素を削除して返却
func removeDuplicate1(args []int) []int {
	results := make([]int, 0, len(args))
	encountered := map[int]bool{}
	for i := 0; i < len(args); i++ {
		if !encountered[args[i]] {
			encountered[args[i]] = true
			results = append(results, args[i])
		}
	}
	return results
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
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	nums := str2IntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])

	fmt.Printf("nums[] = %s\n", printIntArray(nums))
	fmt.Printf("k = %d\n", k)

	timeStart := time.Now()

	result := containsNearbyDuplicate(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

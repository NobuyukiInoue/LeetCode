package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func summaryRanges(nums []int) []string {
	// 0ms
	var res []string

	if nums == nil || len(nums) == 0 {
		return res
	}

	for i := 0; i < len(nums); i++ {
		j := i + 1
		for j < len(nums) && nums[j] == nums[j-1]+1 {
			j++
		}
		if j-i-1 >= 1 {
			res = append(res, strconv.Itoa(nums[i])+"->"+strconv.Itoa(nums[j-1]))
		} else {
			res = append(res, strconv.Itoa(nums[i]))
		}
		i = j - 1
	}
	return res
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

func strArrayToString(data []string) string {
	if len(data) <= 0 {
		return ""
	}

	resultStr := "\"" + data[0] + "\""
	for i := 1; i < len(data); i++ {
		resultStr += ", \"" + data[i] + "\""
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := strToIntArray(flds)
	fmt.Printf("nums = [%s]\n", intArrayToString(nums))

	timeStart := time.Now()

	result := summaryRanges(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", strArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

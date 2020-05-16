package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func buildArray(target []int, n int) []string {
	// 0ms
	res := make([]string, 0)
	pos, i := 1, 0

	for i < len(target) {
		if target[i] == pos {
			res = append(res, "Push")
			i++
		} else {
			res = append(res, "Push")
			res = append(res, "Pop")
		}
		pos++
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

	resultStr := data[0]
	for i := 1; i < len(data); i++ {
		resultStr += ", " + data[i]
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	target := strToIntArray(flds[0])
	n, _ := strconv.Atoi(flds[1])

	fmt.Printf("target = [%s], n = %d\n", intArrayToString(target), n)

	timeStart := time.Now()

	result := buildArray(target, n)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", strArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

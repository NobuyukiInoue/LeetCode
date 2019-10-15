package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func uniqueOccurrences(arr []int) bool {
	d := make(map[int]int)
	for i := 0; i < len(arr); i++ {
		d[arr[i]]++
	}

	var s = make(map[int]int)
	for _, value := range d {
		_, exists := s[value]
		if exists {
			return false
		}
		s[value] = 1
	}
	return true
}

func str2IntArray(flds string) []int {
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

	arr := str2IntArray(flds)

	fmt.Printf("arr = [%s]\n", intArrayToString(arr))
	timeStart := time.Now()

	result := uniqueOccurrences(arr)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

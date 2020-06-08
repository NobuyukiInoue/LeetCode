package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func singleNumber(nums []int) int {
	// 4ms
	ones, twos := 0, 0
	for _, v := range nums {
		ones = (ones ^ v) & ^twos
		twos = (twos ^ v) & ^ones
	}
	return ones
}

func singleNumber2(nums []int) int {
	// 4ms
	mymap := make(map[int]int)

	for _, target := range nums {
		var val int
		v, ok := mymap[target]
		if ok {
			val = v + 1
		} else {
			val = 1
		}
		mymap[target] = val
	}

	for k, v := range mymap {
		if v == 1 {
			return k
		}
	}

	return 0
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
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	nums := strToIntArray(flds)
	fmt.Printf("nums = [%s]\n", intArrayToString(nums))

	timeStart := time.Now()

	result := singleNumber(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

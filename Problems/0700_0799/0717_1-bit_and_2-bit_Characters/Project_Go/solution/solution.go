package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isOneBitCharacter(bits []int) bool {
	i, n := 0, len(bits)-1
	for i < n {
		if bits[i] == 1 {
			i += 2
		} else {
			i++
		}
	}

	if i == n && bits[i] == 0 {
		return true
	} else {
		return false
	}
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
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	bits := str2IntArray(flds)
	fmt.Printf("bits = %s\n", printIntArray(bits))

	timeStart := time.Now()

	result := isOneBitCharacter(bits)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

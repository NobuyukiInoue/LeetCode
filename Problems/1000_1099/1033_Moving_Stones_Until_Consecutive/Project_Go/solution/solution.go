package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func numMovesStones(a int, b int, c int) []int {
	ret := make([]int, 2)
	input := make([]int, 3)

	input[2] = max3(a, b, c)
	input[0] = min3(a, b, c)
	input[1] = a + b + c - input[2] - input[0]

	if input[2]-input[1] == input[1]-input[0] && input[1]-input[0] == 1 {
		return []int{0, 0}
	}

	tmp := 0
	if input[2]-input[1] > input[1]-input[0] {
		tmp = input[1] - input[0]
	} else {
		tmp = input[2] - input[1]
	}

	if tmp <= 2 {
		ret[0] = 1
	} else {
		ret[0] = 2
	}
	ret[1] = input[2] - input[1] - 1 + input[1] - input[0] - 1

	return ret
}

func max3(a int, b int, c int) int {
	if a >= b && a >= c {
		return a
	} else if b >= a && b >= c {
		return b
	} else if c >= a && c >= b {
		return c
	} else {
		return a
	}
}

func min3(a int, b int, c int) int {
	if a <= b && a <= c {
		return a
	} else if b <= a && b <= c {
		return b
	} else if c <= a && c <= b {
		return c
	} else {
		return a
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
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	a, _ := strconv.Atoi(flds[0])
	b, _ := strconv.Atoi(flds[1])
	c, _ := strconv.Atoi(flds[2])
	fmt.Printf("a = %d, b = %d, c = %d\n", a, b, c)

	timeStart := time.Now()

	result := numMovesStones(a, b, c)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", printIntArray(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

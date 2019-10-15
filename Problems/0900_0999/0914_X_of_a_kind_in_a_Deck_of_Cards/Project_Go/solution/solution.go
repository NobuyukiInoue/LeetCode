package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func hasGroupsSizeX(deck []int) bool {
	size := len(deck)

	count := make(map[int]int, size)
	for _, card := range deck {
		count[card]++
	}

	d := count[deck[0]]

	for _, c := range count {
		d = gcd(d, c)
		if d == 1 {
			return false
		}
	}

	return true
}

// 最大公约数
func gcd(a, b int) int {
	if a < b {
		a, b = b, a
	}
	for b != 0 {
		a, b = b, a%b
	}
	return a
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
	flds := strings.Replace(temp, "]", "", -1)

	deck := str2IntArray(flds)
	fmt.Printf("deck = %s\n", printIntArray(deck))

	timeStart := time.Now()

	result := hasGroupsSizeX(deck)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

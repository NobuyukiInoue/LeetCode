package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func corpFlightBookings(bookings [][]int, n int) []int {
	// 140ms
	res := make([]int, n)
	for _, flds := range bookings {
		res[flds[0]-1] += flds[2]
		if flds[1] < n {
			res[flds[1]] -= flds[2]
		}
	}
	for i := 1; i < n; i++ {
		res[i] += res[i-1]
	}
	return res
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
	temp = strings.Replace(temp, "[[[", "", -1)
	flds := strings.Split(temp, "]],[")
	bookings_str := strings.Split(flds[0], "],[")

	bookings := make([][]int, len(bookings_str))
	for i := 0; i < len(bookings_str); i++ {
		bookings[i] = str2IntArray(bookings_str[i])
	}

	n, _ := strconv.Atoi(strings.Replace(flds[1], "]]", "", -1))

	fmt.Printf("bookings = [")
	for i, _ := range bookings {
		if i == 0 {
			fmt.Printf("[%s]", printIntArray(bookings[i]))
		} else {
			fmt.Printf(",[%s]", printIntArray(bookings[i]))
		}
	}
	fmt.Printf("]\n")
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := corpFlightBookings(bookings, n)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", printIntArray(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

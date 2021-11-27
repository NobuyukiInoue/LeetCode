package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func getLastMoment(n int, left []int, right []int) int {
	// 20ms
	res := 0
	for _, i := range left {
		res = myMax(res, i)
	}
	for _, i := range right {
		res = myMax(res, n-i)
	}
	return res
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	n, _ := strconv.Atoi(flds[0])
	left := StringToIntArray(flds[1])
	right := StringToIntArray(flds[2])
	fmt.Printf("n = %d, left = [%s], right = [%s]\n", n, IntArrayToString(left), IntArrayToString(right))

	timeStart := time.Now()

	result := getLastMoment(n, left, right)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

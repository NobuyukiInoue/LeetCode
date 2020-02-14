package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func nthUglyNumber(n int, a int, b int, c int) int {
	ans := 0
	arr := []int{a, b, c}

	for _, k := range arr {
		ans = binarySearch(n, k, arr)
		if ans > 0 {
			break
		}
	}
	return ans
}

func gcd(n int, m int) int {
	if m == 0 {
		return n
	}
	return gcd(m, n%m)
}

func binarySearch(n int, k int, arr []int) int {
	left, right := 1, n
	a := arr[0] * arr[1] / gcd(arr[0], arr[1])
	b := arr[0] * arr[2] / gcd(arr[0], arr[2])
	c := arr[1] * arr[2] / gcd(arr[1], arr[2])
	d := a * arr[2] / gcd(a, arr[2])
	for left <= right {
		mid := (left + right) / 2
		val := mid * k
		m := val/arr[0] + val/arr[1] + val/arr[2] - val/a - val/b - val/c + val/d
		if m == n {
			return val
		} else if m < n {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return -1
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	n, _ := strconv.Atoi(flds[0])
	a, _ := strconv.Atoi(flds[1])
	b, _ := strconv.Atoi(flds[2])
	c, _ := strconv.Atoi(flds[3])

	fmt.Printf("n = %d, a = %d, b = %d, c = %d\n", n, a, b, c)
	timeStart := time.Now()

	result := nthUglyNumber(n, a, b, c)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func minMovesToCaptureTheQueen(a int, b int, c int, d int, e int, f int) int {
	// 0ms
	if a == e && !(a == c && d > myMin(b, f) && d < myMax(b, f)) {
		return 1
	}
	if b == f && !(b == d && c > myMin(a, e) && c < myMax(a, e)) {
		return 1
	}
	if c+d == e+f && !(c+d == a+b && a > myMin(c, e) && a < myMax(c, e)) {
		return 1
	}
	if c-d == e-f && !(c-d == a-b && a > myMin(c, e) && a < myMax(c, e)) {
		return 1
	}
	return 2
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func myMin(a, b int) int {
	if a < b {
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
	a, _ := strconv.Atoi(flds[0])
	b, _ := strconv.Atoi(flds[1])
	c, _ := strconv.Atoi(flds[2])
	d, _ := strconv.Atoi(flds[3])
	e, _ := strconv.Atoi(flds[4])
	f, _ := strconv.Atoi(flds[5])

	fmt.Printf("a = %d, b = %d, c = %d, d = %d, e = %d, f = %d\n", a, b, c, d, e, f)

	timeStart := time.Now()

	result := minMovesToCaptureTheQueen(a, b, c, d, e, f)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

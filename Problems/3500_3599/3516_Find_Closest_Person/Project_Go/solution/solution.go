package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findClosest(x int, y int, z int) int {
	// 0ms
	dif_x, dif_y := myAbs(z-x), myAbs(z-y)
	if dif_x < dif_y {
		return 1
	} else if dif_x > dif_y {
		return 2
	} else {
		return 0
	}
}

func myAbs(n int) int {
	if n >= 0 {
		return n
	}
	return -n
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	x, _ := strconv.Atoi(flds[0])
	y, _ := strconv.Atoi(flds[1])
	z, _ := strconv.Atoi(flds[2])
	fmt.Printf("x = %d, y = %d, z = %d\n", x, y, z)

	timeStart := time.Now()

	result := findClosest(x, y, z)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

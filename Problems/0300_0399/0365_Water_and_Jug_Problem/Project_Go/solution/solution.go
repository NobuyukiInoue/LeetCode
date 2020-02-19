package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func canMeasureWater(x int, y int, z int) bool {
	// 0ms
	if x+y < z {
		return false
	}
	if x == z || y == z || x+y == z {
		return true
	}
	return z%GCD(x, y) == 0
}

func GCD(a int, b int) int {
	for b != 0 {
		temp := b
		b = a % b
		a = temp
	}
	return a
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	x, _ := strconv.Atoi(flds[0])
	y, _ := strconv.Atoi(flds[1])
	z, _ := strconv.Atoi(flds[2])
	fmt.Printf("x = %d, y = %d, z = %d\n", x, y, z)

	timeStart := time.Now()

	result := canMeasureWater(x, y, z)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

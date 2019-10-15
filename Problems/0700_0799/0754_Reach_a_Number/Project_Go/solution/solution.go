package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func reachNumber(target int) int {
	targetAbs := int(math.Abs(float64(target)))
	sqrtVal := int(math.Sqrt(2 * float64(targetAbs)))

	if sqrtVal*(sqrtVal+1) < 2*targetAbs {
		sqrtVal++
	}
	if target%2 == 0 {
		for sqrtVal%4 != 0 && (sqrtVal+1)%4 != 0 {
			sqrtVal++
		}
	} else {
		for sqrtVal%4 == 0 || (sqrtVal+1)%4 == 0 {
			sqrtVal++
		}
	}

	return sqrtVal
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	target, _ := strconv.Atoi(flds)

	fmt.Printf("target = %d\n", target)

	timeStart := time.Now()

	result := reachNumber(target)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

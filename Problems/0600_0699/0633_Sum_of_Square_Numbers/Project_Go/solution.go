package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func judgeSquareSum(c int) bool {
	i := 0
	j := int(math.Sqrt(float64(c)))

	for i <= j {
		sum := i*i + j*j
		if i*i+j*j == c {
			return true
		} else if sum < c {
			i++
		} else {
			j--
		}
	}

	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	c, _ := strconv.Atoi(flds)

	fmt.Printf("c = %d\n", c)

	timeStart := time.Now()

	result := judgeSquareSum(c)
	fmt.Printf("result = %s\n", strconv.FormatBool(result))

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strings"
	"time"
)

func categorizeBox(length int, width int, height int, mass int) string {
	// 0ms
	bulky := myMax(length, myMax(width, height)) >= 1e4 || length*width*height >= 1e9
	heavy := (mass >= 100)
	if bulky && heavy {
		return "Both"
	}
	if bulky {
		return "Bulky"
	}
	if heavy {
		return "Heavy"
	}
	return "Neither"
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	length, width, height, mass := nums[0], nums[1], nums[2], nums[3]
	fmt.Printf("length = %d, width = %d, height = %d, mass = %d\n", length, width, height, mass)

	timeStart := time.Now()

	result := categorizeBox(length, width, height, mass)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func maxHeightOfTriangle(red int, blue int) int {
	// 4ms
	if red < blue {
		return maxHeightOfTriangle(blue, red)
	}
	h1 := int(math.Sqrt(float64(blue*4 + 1)))
	h2 := int(math.Sqrt(float64(blue))) * 2
	if int(math.Pow(float64(h1+1), 2.0))/4 <= red {
		return h1
	}
	if int((math.Pow(float64(h2+1), 2.0))-1)/4 <= red {
		return h2
	}
	if int(math.Pow(float64(h1-1), 2.0))/4 <= red {
		return h1 - 1
	}
	return h2 - 1
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	red, _ := strconv.Atoi(flds[0])
	blue, _ := strconv.Atoi(flds[1])
	fmt.Printf("red = %d, blue = %d\n", red, blue)

	timeStart := time.Now()

	result := maxHeightOfTriangle(red, blue)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

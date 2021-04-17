package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func squareIsWhite(coordinates string) bool {
	// 0ms
	if (coordinates[0] + coordinates[1]) % 2 == 0 {
		return false
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	coordinates := strings.Replace(temp, "]", "", -1)
	fmt.Printf("coordinates = %s\n", coordinates)

	timeStart := time.Now()

	result := squareIsWhite(coordinates)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

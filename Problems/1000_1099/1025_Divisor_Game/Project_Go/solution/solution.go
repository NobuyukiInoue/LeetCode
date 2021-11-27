package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func divisorGame(n int) bool {
	// 0ms
	return n%2 == 0
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)

	n, _ := strconv.Atoi(fld)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := divisorGame(n)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func getNoZeroIntegers(n int) []int {
	// 4ms
	for a := 1; a < n; a++ {
		b := n - a
		if strings.Index(strconv.Itoa(a), "0") < 0 && strings.Index(strconv.Itoa(b), "0") < 0 {
			return []int{a, b}
		}
	}
	return []int{}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)

	n, _ := strconv.Atoi(fld)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := getNoZeroIntegers(n)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

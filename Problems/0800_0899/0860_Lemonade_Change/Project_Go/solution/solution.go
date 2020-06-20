package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func lemonadeChange(bills []int) bool {
	five, ten := 0, 0
	for _, value := range bills {
		if value == 5 {
			five++
		} else if value == 10 {
			five--
			ten++
		} else if ten > 0 {
			ten--
			five--
		} else {
			five -= 3
		}
		if five < 0 {
			return false
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	bills := StringToIntArray(flds)
	fmt.Printf("bills = [%s]\n", IntArrayToString(bills))

	timeStart := time.Now()

	result := lemonadeChange(bills)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

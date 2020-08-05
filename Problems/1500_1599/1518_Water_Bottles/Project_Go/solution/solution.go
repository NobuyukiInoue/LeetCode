package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func numWaterBottles(numBottles int, numExchange int) int {
	// 0ms
	exchangedBottles := 0
	for numBottles >= numExchange {
		divBottles := numBottles / numExchange
		exchangedBottles += divBottles*numExchange
		numBottles = numBottles % numExchange + divBottles
	}
	return exchangedBottles + numBottles
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	numBottles, _  := strconv.Atoi(flds[0])
	numExchange, _ := strconv.Atoi(flds[1])

	timeStart := time.Now()

	result := numWaterBottles(numBottles, numExchange)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

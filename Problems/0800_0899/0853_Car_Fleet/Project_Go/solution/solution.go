package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func carFleet(target int, position []int, speed []int) int {
	return 0
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	target, _ := strconv.Atoi(strings.Replace(flds[0], "[[", "", -1))
	position := StringToIntArray(flds[1])
	speed := StringToIntArray(strings.Replace(flds[2], "]]", "", -1))
	fmt.Printf("target = %d, position = [%s], speed = [%s]\n", target, IntArrayToString(position), IntArrayToString(speed))

	timeStart := time.Now()

	result := carFleet(target, position, speed)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

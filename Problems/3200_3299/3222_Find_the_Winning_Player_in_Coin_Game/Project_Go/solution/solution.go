package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func losingPlayer(x int, y int) string {
	// 0ms
	cnt := 0
	for x > 0 && y > 3 {
		x--
		y -= 4
		cnt++
	}
	if cnt%2 == 1 {
		return "Alice"
	}
	return "Bob"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	x, _ := strconv.Atoi(flds[0])
	y, _ := strconv.Atoi(flds[1])
	fmt.Printf("x = %d, y = %d\n", x, y)

	timeStart := time.Now()

	result := losingPlayer(x, y)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

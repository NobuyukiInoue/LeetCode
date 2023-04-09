package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func distMoney(money int, children int) int {
	// 8ms - 14ms
	money -= children
	if money < 0 {
		return -1
	}
	if money/7 == children && money%7 == 0 {
		return children
	}
	if money/7 == children-1 && money%7 == 3 {
		return children - 2
	}
	return myMin(children-1, money/7)
}

func myMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	money, _ := strconv.Atoi(flds[0])
	children, _ := strconv.Atoi(flds[1])
	fmt.Printf("money = %d, time = %d\n", money, children)

	timeStart := time.Now()

	result := distMoney(money, children)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func distanceTraveled(mainTank int, additionalTank int) int {
	// 8ms - 27ms
	return (mainTank + myMin((mainTank-1)/4, additionalTank)) * 10
}

func distanceTraveled2(mainTank int, additionalTank int) int {
	// 19ms - 30m
	ans := 0
	for mainTank >= 5 {
		mainTank -= 5
		ans += 50
		if additionalTank >= 1 {
			additionalTank--
			mainTank++
		}
	}
	return ans + mainTank*10
}

func myMin(a, b int) int {
	if a <= b {
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

	mainTank, _ := strconv.Atoi(flds[0])
	additionalTank, _ := strconv.Atoi(flds[1])
	fmt.Printf("mainTank = %d, additionalTank = %d\n", mainTank, additionalTank)

	timeStart := time.Now()

	result := distanceTraveled(mainTank, additionalTank)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

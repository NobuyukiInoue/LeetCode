package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func fractionToDecimal(numerator int, denominator int) string {
	// 0ms
	result := ""

	if numerator == 0 {
		return "0"
	}

	if numerator < 0 && denominator < 0 {
		numerator *= -1
		denominator *= -1
	} else if numerator < 0 || denominator < 0 {
		if numerator < 0 {
			numerator *= -1
		} else {
			denominator *= -1
		}
		result += "-"
	}

	if numerator < 0 || denominator < 0 {
		result += "-"
	}
	result += strconv.Itoa(numerator / denominator)
	reminder := numerator % denominator
	if reminder == 0 {

		return result
	}
	result += "."

	m := make(map[int]int, 0)

	for reminder != 0 {
		if v, ok := m[reminder]; ok {
			result = string(result[0:v]) + "(" + string(result[v:]) + ")"
			break
		} else {
			m[reminder] = len(result)
		}
		reminder = reminder * 10
		result += strconv.Itoa(reminder / denominator)
		reminder %= denominator
	}
	return result
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	numerator, _ := strconv.Atoi(flds[0])
	denominator, _ := strconv.Atoi(flds[1])
	fmt.Printf("gifts = %d, denominator = %d\n", numerator, denominator)

	timeStart := time.Now()

	result := fractionToDecimal(numerator, denominator)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func hasGroupsSizeX(deck []int) bool {
	size := len(deck)

	count := make(map[int]int, size)
	for _, card := range deck {
		count[card]++
	}

	d := count[deck[0]]

	for _, c := range count {
		d = gcd(d, c)
		if d == 1 {
			return false
		}
	}

	return true
}

// 最大公约数
func gcd(a, b int) int {
	if a < b {
		a, b = b, a
	}
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	deck := StringToIntArray(flds)
	fmt.Printf("deck = [%s]\n", IntArrayToString(deck))

	timeStart := time.Now()

	result := hasGroupsSizeX(deck)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

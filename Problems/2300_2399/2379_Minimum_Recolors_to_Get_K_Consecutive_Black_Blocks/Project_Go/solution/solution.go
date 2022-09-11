package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func minimumRecolors(blocks string, k int) int {
	// 3ms - 4ms
	lo, white, mi := -1, 0, math.MaxInt32
	for i, c := range blocks {
		if c == 'W' {
			white++
		}
		if i-lo >= k {
			mi = myMin(white, mi)
			lo++
			if blocks[lo] == 'W' {
				white--
			}
		}
	}
	return mi
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	blocks := flds[0]
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("blocks = [%s], k = %d\n", blocks, k)

	timeStart := time.Now()

	result := minimumRecolors(blocks, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func hasAllCodes(s string, k int) bool {
	// 135ms - 141ms
	codes := make(map[string]bool, 0)
	for i := 0; i < len(s)-k+1; i++ {
		codes[s[i:i+k]] = true
	}
	return len(codes) == int(math.Pow(2, float64(k)))
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	s := flds[0]
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("s = \"%s\", k = %d\n", s, k)

	timeStart := time.Now()

	result := hasAllCodes(s, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

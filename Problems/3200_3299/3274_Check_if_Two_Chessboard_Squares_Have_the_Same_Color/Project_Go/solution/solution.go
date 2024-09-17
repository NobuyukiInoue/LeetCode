package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func checkTwoChessboards(coordinate1 string, coordinate2 string) bool {
	// 3ms
	d1 := coordinate1[0] + coordinate1[1]
	d2 := coordinate2[0] + coordinate2[1]
	return d1%2 == d2%2
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	flds := strings.Split(temp, "],[")

	coordinate1 := flds[0]
	coordinate2 := flds[1]
	fmt.Printf("coordinate1 = \"%s\", coordinate2 = \"%s\"\n", coordinate1, coordinate2)

	timeStart := time.Now()

	result := checkTwoChessboards(coordinate1, coordinate2)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

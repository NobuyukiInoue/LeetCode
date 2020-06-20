package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isRectangleOverlap(rec1 []int, rec2 []int) bool {
	return rec1[0] < rec2[2] && rec2[0] < rec1[2] && rec1[1] < rec2[3] && rec2[1] < rec1[3]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	rec1 := StringToIntArray(flds[0])
	rec2 := StringToIntArray(flds[1])
	fmt.Printf("rec1 = [%s]\n", IntArrayToString(rec1))
	fmt.Printf("rec2 = [%s]\n", IntArrayToString(rec2))

	timeStart := time.Now()

	result := isRectangleOverlap(rec1, rec2)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

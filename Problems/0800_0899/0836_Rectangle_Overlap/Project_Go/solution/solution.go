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

func IntArray2string(arr []int) string {
	if len(arr) <= 0 {
		return ""
	}

	resultStr := "["
	for i := 0; i < len(arr); i++ {
		if i > 0 {
			resultStr += ","
		}
		resultStr += strconv.Itoa(arr[i])
	}

	return resultStr + "]"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")

	pt1 := strings.Split(flds[0], ",")
	rec1 := make([]int, len(pt1))
	for i := 0; i < len(pt1); i++ {
		rec1[i], _ = strconv.Atoi(pt1[i])
	}

	pt2 := strings.Split(flds[1], ",")
	rec2 := make([]int, len(pt2))
	for i := 0; i < len(pt2); i++ {
		rec2[i], _ = strconv.Atoi(pt2[i])
	}

	fmt.Printf("rec1 = %s\n", IntArray2string(rec1))
	fmt.Printf("rec2 = %s\n", IntArray2string(rec2))

	timeStart := time.Now()

	result := isRectangleOverlap(rec1, rec2)
	fmt.Printf("result = %s\n", strconv.FormatBool(result))

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

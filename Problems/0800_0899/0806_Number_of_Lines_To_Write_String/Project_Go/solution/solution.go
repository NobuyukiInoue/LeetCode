package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func numberOfLines(widths []int, S string) []int {
	res, cur := 1, 0
	for i := 0; i < len(S); i++ {
		width := widths[S[i]-'a']
		if cur+width > 100 {
			res++
		}
		if cur+width > 100 {
			cur = width
		} else {
			cur += width
		}
	}

	return []int{res, cur}
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
	widthStr := strings.Split(flds[0], ",")

	widths := make([]int, len(widthStr))
	for i := 0; i < len(widthStr); i++ {
		width_temp, _ := strconv.Atoi(widthStr[i])
		widths[i] = width_temp
	}

	S := flds[1]

	fmt.Printf("widths[] = %s\n", IntArray2string(widths))
	fmt.Printf("S = %s\n", S)

	timeStart := time.Now()

	result := numberOfLines(widths, S)
	fmt.Printf("result = %s\n", IntArray2string(result))

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

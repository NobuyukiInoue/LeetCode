package solution

import (
	"fmt"
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

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	widths := StringToIntArray(flds[0])
	fmt.Printf("widths = [%s]\n", IntArrayToString(widths))

	S := flds[1]
	fmt.Printf("S = %s\n", S)

	timeStart := time.Now()

	result := numberOfLines(widths, S)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

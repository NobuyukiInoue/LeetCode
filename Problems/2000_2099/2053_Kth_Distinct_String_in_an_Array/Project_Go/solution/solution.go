package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func kthDistinct(arr []string, k int) string {
	// 8ms
	mymap := make(map[string]int)
	for _, word := range arr {
		mymap[word]++
	}
	kth := 0
	for _, word := range arr {
		if mymap[word] == 1 {
			kth++
			if kth == k {
				return word
			}
		}
	}
	return ""
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	arr := strings.Split(flds[0], ",")
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("arr = [%s], k = %d\n", StringArrayToString(arr), k)

	timeStart := time.Now()

	result := kthDistinct(arr, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

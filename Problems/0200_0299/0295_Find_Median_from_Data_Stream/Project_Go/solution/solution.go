package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

import "./medianfinder"

func medianFinderMain(ope []string, params []string) {
	if len(ope) != len(params) {
		return
	}

	if len(ope) <= 0 || len(params) <= 0 {
		return
	}

	mf := medianfinder.Constructor()
	for i, _ := range ope {
		if ope[i] == "MedianFinder" {
			fmt.Printf("MedianFinder()\n")

		} else if ope[i] == "addNum" {
			num, _ := strconv.Atoi(params[i])
			mf.AddNum(num)
			fmt.Printf("addNum(%s)\n", params[i])

		} else if ope[i] == "findMedian" {
			res := mf.FindMedian()
			fmt.Printf("medianFinder() ... %f\n", res)

		}
	}
}

func strArrayToString(data []string) string {
	if len(data) <= 0 {
		return ""
	}

	res := "[" + data[0]
	for i := 1; i < len(data); i++ {
		res += ", \"" + data[i] + "\""
	}

	return res + "]"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	flds := strings.Split(temp, "],[[")

	flds0 := strings.Replace(flds[0], "[", "", -1)
	flds0 = strings.Replace(flds0, "[", "", -1)
	flds0 = strings.Replace(flds0, "]", "", -1)
	ope := strings.Split(flds0, ",")

	flds1 := strings.Replace(flds[1], "]]", "", -1)
	params := strings.Split(flds1, "],[")

	fmt.Printf("ope = %s\n", strArrayToString(ope))
	fmt.Printf("params = %s\n", strArrayToString(params))

	timeStart := time.Now()

	medianFinderMain(ope, params)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

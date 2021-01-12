package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func maximumUnits(boxTypes [][]int, truckSize int) int {
	// 20ms
	sort.Slice(boxTypes, func(i int, j int) bool { return boxTypes[j][1] < boxTypes[i][1] })
	cntUnit, cntBox := 0, 0
	for _, target := range boxTypes {
		if cntBox+target[0] <= truckSize {
			cntUnit += target[0] * target[1]
			cntBox += target[0]
		} else {
			var i int
			if target[0] <= truckSize-cntBox {
				i = target[0]
			} else {
				i = truckSize - cntBox
			}
			cntUnit += target[1] * i
			cntBox += i
		}
		if cntBox >= truckSize {
			break
		}
	}
	return cntUnit
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[[", "", -1)
	flds := strings.Split(temp, "]],[")

	flds0 := strings.Split(flds[0], "],[")
	boxTypes := make([][]int, len(flds0))
	for i := 0; i < len(boxTypes); i++ {
		boxTypes[i] = StringToIntArray(flds0[i])
	}
	truckSize, _ := strconv.Atoi(strings.Replace(flds[1], "]", "", -1))
	fmt.Printf("boxTypes  = %s\n", IntIntArrayToString(boxTypes))
	fmt.Printf("truckSize = %d\n", truckSize)

	timeStart := time.Now()

	result := maximumUnits(boxTypes, truckSize)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

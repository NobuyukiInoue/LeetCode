package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func constructRectangle(area int) []int {
	mid := int(math.Sqrt(float64(area)))
	for area%mid != 0 {
		mid--
	}

	return []int{area / mid, mid}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	area, _ := strconv.Atoi(flds)
	fmt.Printf("area = %d\n", area)

	timeStart := time.Now()

	result := constructRectangle(area)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strings"
	"time"
)

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	flds_str := strings.Replace(temp, ", ", ",", -1)

	flds := createListNestedInteger(flds_str)
	fmt.Printf("nums = %s\n", listNestedIntegerToString(flds))

	timeStart := time.Now()

	result := getNestedIterator(flds)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

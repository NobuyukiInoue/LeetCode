package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isLongPressedName(name, typed string) bool {
	if name == typed {
		return true
	}

	nameSize := len(name)
	typedSize := len(typed)

	i, j := 0, 0
	for i < nameSize {
		c := name[i]
		pressMore := 0

		for i < nameSize && name[i] == c {
			i++
			pressMore--
		}

		for j < typedSize && typed[j] == c {
			j++
			pressMore++
		}

		if pressMore < 0 {
			return false
		}

	}

	return j == typedSize
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	name, typed := flds[0], flds[1]
	fmt.Printf("name = %s, typed = %s\n", name, typed)

	timeStart := time.Now()

	result := isLongPressedName(name, typed)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

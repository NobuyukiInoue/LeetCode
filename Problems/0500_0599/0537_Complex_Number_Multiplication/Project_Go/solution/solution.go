package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func complexNumberMultiply(num1 string, num2 string) string {
	// 0ms
	flds1 := strings.Split(num1, "+")
	flds2 := strings.Split(num2, "+")
	n1r, _ := strconv.Atoi(flds1[0])
	n1i, _ := strconv.Atoi(flds1[1][:len(flds1[1])-1])
	n2r, _ := strconv.Atoi(flds2[0])
	n2i, _ := strconv.Atoi(flds2[1][:len(flds2[1])-1])
	re := n1r*n2r - n1i*n2i
	im := n1r*n2i + n1i*n2r
	return strconv.Itoa(re) + "+" + strconv.Itoa(im) + "i"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	num1, num2 := flds[0], flds[1]
	fmt.Printf("num1 = \"%s\", num2 = \"%s\"\n", num1, num2)

	timeStart := time.Now()

	result := complexNumberMultiply(num1, num2)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

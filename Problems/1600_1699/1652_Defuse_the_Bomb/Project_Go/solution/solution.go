package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func decrypt(code []int, k int) []int {
	// 0ms
	res := make([]int, len(code))

	if k == 0 {
		return res
	}

	codeLength := len(code)
	start, end, sum := 1, k, 0

	if k < 0 {
		k = -k
		start = codeLength - k
		end = codeLength - 1
	}

	for i := start; i <= end; i++ {
		sum += code[i]
	}

	for i := 0; i < codeLength; i++ {
		res[i] = sum
		sum -= code[start % codeLength]
		start++
		end++
		sum += code[end % codeLength]
	}

	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	code := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("code = [%s], k = %d\n", IntArrayToString(code), k)

	timeStart := time.Now()

	result := decrypt(code, k)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

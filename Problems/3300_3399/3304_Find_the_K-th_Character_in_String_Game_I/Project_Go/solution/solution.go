package solution

import (
	"fmt"
	"math/bits"
	"strconv"
	"strings"
	"time"
)

func kthCharacter(k int) byte {
	// 0ms
	return byte('a' + bits.OnesCount32(uint32(k-1)))
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	k, _ := strconv.Atoi(flds)
	fmt.Printf("k = %d\n", k)

	timeStart := time.Now()

	result := kthCharacter(k)

	timeEnd := time.Now()

	fmt.Printf("result = %c\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

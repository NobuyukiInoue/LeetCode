package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func canIWin(maxChoosableInteger int, desiredTotal int) bool {
	// 16ms
	if maxChoosableInteger > desiredTotal {
		return true
	}
	if (maxChoosableInteger*(maxChoosableInteger+1))>>1 < desiredTotal {
		return false
	}
	return helper(0, uint(maxChoosableInteger), uint(desiredTotal), make([]int, 1<<uint(maxChoosableInteger)))
}

func helper(bits uint, maxChoosableInteger uint, desiredTotal uint, dp []int) bool {
	if dp[bits] != 0 {
		return dp[bits] == 1
	}
	for i := uint(0); i < maxChoosableInteger; i++ {
		if ((bits>>i)&1) == 0 && (i+1 >= desiredTotal || !helper(bits|(1<<i), maxChoosableInteger, desiredTotal-i-1, dp)) {
			dp[bits] = 1
			return true
		}
	}
	dp[bits] = -1
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	maxChoosableInteger, _ := strconv.Atoi(flds[0])
	desiredTotal, _ := strconv.Atoi(flds[1])
	fmt.Printf("maxChoosableInteger = %d, desireTotal = %d\n", maxChoosableInteger, desiredTotal)

	timeStart := time.Now()

	result := canIWin(maxChoosableInteger, desiredTotal)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

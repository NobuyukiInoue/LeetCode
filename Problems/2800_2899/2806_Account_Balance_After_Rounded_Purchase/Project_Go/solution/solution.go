package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func accountBalanceAfterPurchase(purchaseAmount int) int {
	// 0ms
	return 100 - ((purchaseAmount+5)/10)*10
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)
	purchaseAmount, _ := strconv.Atoi(fld)
	fmt.Printf("purchaseAmount = %d\n", purchaseAmount)

	timeStart := time.Now()

	result := accountBalanceAfterPurchase(purchaseAmount)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

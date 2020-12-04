package solution

import (
	"fmt"
	"strings"
	"time"
)

func maximumWealth(accounts [][]int) int {
	// 4ms
	ans := 0
	for _, account := range(accounts) {
		temp := arraySum(account)
		if temp > ans {
			ans = temp
		}
	}
	return ans
}

func arraySum(data []int) int {
	if data == nil {
		return 0
	}

	if len(data) <= 0 {
		return 0
	}

	total := data[0]
	for i := 1; i < len(data); i++ {
		total += data[i]
	}

	return total
}


func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	accounts := make([][]int, len(flds))
	for i := 0; i < len(accounts); i++ {
		accounts[i] = StringToIntArray(flds[i])
	}
	fmt.Printf("accounts = %s\n", IntIntArrayToString(accounts))

	timeStart := time.Now()

	result := maximumWealth(accounts)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

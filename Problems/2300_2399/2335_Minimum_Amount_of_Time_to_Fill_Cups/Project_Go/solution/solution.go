package solution

import (
	"fmt"
	"strings"
	"time"
)

func fillCups(amount []int) int {
	// 0ms - 2ms
	m_max, total := 0, 0
	for _, num := range amount {
		m_max = myMax(num, m_max)
		total += num
	}
	return myMax(m_max, (total+1)/2)
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	amount := StringToIntArray(flds)
	fmt.Printf("amount = [%s]\n", IntArrayToString(amount))

	timeStart := time.Now()

	result := fillCups(amount)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

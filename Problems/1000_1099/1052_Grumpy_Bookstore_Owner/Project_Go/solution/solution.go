package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func maxSatisfied(customers []int, grumpy []int, minutes int) int {
	// 28ms - 33ms
	total := 0
	n := len(customers)
	for i, _ := range customers {
		total += customers[i] * (1 - grumpy[i])
		grumpy[i] = customers[i] * grumpy[i]
	}
	m_customers := 0
	for i := 0; i < minutes; i++ {
		m_customers += grumpy[i]
	}
	save := m_customers
	for i := minutes; i < n; i++ {
		save += grumpy[i] - grumpy[i-minutes]
		if save > m_customers {
			m_customers = save
		}
	}
	return total + m_customers
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	customers := StringToIntArray(flds[0])
	grumpy := StringToIntArray(flds[1])
	minutes, _ := strconv.Atoi(flds[2])
	fmt.Printf("customers = [%s], grumpy = [%s], minutes = %d\n", IntArrayToString(customers), IntArrayToString(grumpy), minutes)

	timeStart := time.Now()

	result := maxSatisfied(customers, grumpy, minutes)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func countDaysTogether(arriveAlice string, leaveAlice string, arriveBob string, leaveBob string) int {
	// 0ms - 3ms
	month := []int{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
	for i := 1; i < len(month); i++ {
		month[i] = month[i-1] + month[i]
	}
	aa_m, _ := strconv.Atoi(arriveAlice[:2])
	aa_d, _ := strconv.Atoi(arriveAlice[3:])
	al_m, _ := strconv.Atoi(leaveAlice[:2])
	al_d, _ := strconv.Atoi(leaveAlice[3:])
	ba_m, _ := strconv.Atoi(arriveBob[:2])
	ba_d, _ := strconv.Atoi(arriveBob[3:])
	bl_m, _ := strconv.Atoi(leaveBob[:2])
	bl_d, _ := strconv.Atoi(leaveBob[3:])
	alice_a := month[aa_m-1] + aa_d
	alice_l := month[al_m-1] + al_d
	bob_a := month[ba_m-1] + ba_d
	bob_l := month[bl_m-1] + bl_d
	return myMax(myMin(alice_l, bob_l)-myMax(alice_a, bob_a)+1, 0)
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func myMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	arriveAlice, leaveAlice, arriveBob, leaveBob := flds[0], flds[1], flds[2], flds[3]
	fmt.Printf("arriveAlice = %s, leaveAlice = %s, arriveBob = %s, leaveBob = %s\n", arriveAlice, leaveAlice, arriveBob, leaveBob)

	timeStart := time.Now()

	result := countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

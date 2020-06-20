package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

type Cmds struct {
	cmd string
	arg string
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	flds := strings.Split(temp, "],[[")

	temp1 := strings.Replace(flds[0], " ", "", -1)
	temp1 = strings.Replace(temp1, "\"", "", -1)
	temp1 = strings.Replace(temp1, "[", "", -1)
	temp1 = strings.Replace(temp1, "]", "", -1)
	flds1 := strings.Split(temp1, ",")

	temp2 := strings.Replace(flds[1], " ", "", -1)
	temp2 = strings.Replace(temp2, "\"", "", -1)
	temp2 = strings.Replace(temp2, "[", "", -1)
	temp2 = strings.Replace(temp2, "]", "", -1)
	flds2 := strings.Split(temp2, ",")

	if len(flds1) != len(flds2) {
		fmt.Printf("cmds count is not equal args count.\n")
		return
	}

	execList := make([]Cmds, len(flds1))

	for i := 0; i < len(flds1); i++ {
		fmt.Printf("cmd[%d] = %s(%s)\n", i, flds1[i], flds2[i])
		execList[i] = Cmds{string(flds1[i]), string(flds2[i])}
	}

	fmt.Printf("\n")

	timeStart := time.Now()

	rc := Constructor()
	result := make([]int, len(execList))

	for i := 0; i < len(execList); i++ {
		if execList[i].cmd == "RecentCounter" {
			//rc = new RecentCounter();
			result[i] = -1
			fmt.Printf("Execute ... %s()\n", execList[i].cmd)
		} else if execList[i].cmd == "ping" {
			val, _ := strconv.Atoi(execList[i].arg)
			result[i] = rc.Ping(val)
			fmt.Printf("Execute ... %s(%s)\n", execList[i].cmd, execList[i].arg)
		} else {
			fmt.Printf("%s is not found.\n", execList[i].cmd)
			return
		}
	}

	timeEnd := time.Now()
	fmt.Printf("\nresult = %s\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

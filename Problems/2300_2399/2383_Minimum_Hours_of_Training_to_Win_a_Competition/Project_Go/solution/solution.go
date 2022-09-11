package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func minNumberOfHours(initialEnergy int, initialExperience int, energy []int, experience []int) int {
	// 2ms
	enery_required, total_energy := 0, 0
	for _, en := range energy {
		total_energy += en
	}

	if total_energy >= initialEnergy {
		enery_required = total_energy - initialEnergy + 1
	}

	exp_required := 0
	for _, exp := range experience {
		training_exp := 0
		if initialExperience <= exp {
			training_exp = exp - initialExperience + 1
			exp_required += training_exp
		}
		initialExperience += exp + training_exp
	}
	return enery_required + exp_required
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	initialEnergy, _ := strconv.Atoi(flds[0])
	initialExperience, _ := strconv.Atoi(flds[1])
	energy := StringToIntArray(flds[2])
	experience := StringToIntArray(flds[3])
	fmt.Printf("initialEnergy = %d, initialExperience = %d, energy = [%s], experience = [%s]\n", initialEnergy, initialExperience, IntArrayToString(energy), IntArrayToString(experience))

	timeStart := time.Now()

	result := minNumberOfHours(initialEnergy, initialExperience, energy, experience)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

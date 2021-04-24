package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

type scoreToAge struct {
    score int
    age int
}

func bestTeamScore(scores []int, ages []int) int {
    sa := []scoreToAge{}
    for i := 0; i < len(scores); i++ {
        sa = append(sa, scoreToAge{
            score : scores[i],
            age : ages[i],
        })  
    }
    
    sort.Slice(sa, func(i, j int) bool {
        if sa[i].age == sa[j].age {
            return sa[i].score < sa[j].score
        }
        return sa[i].age < sa[j].age        
    })

    dp := make([]int, len(scores))
    dp[0] = sa[0].score
    maxScore := dp[0]
    for i := 1; i < len(scores); i++ {
        maxVal := 0
        for j := 0; j < i; j++ {
            val := sa[i].score
            if sa[i].score >= sa[j].score {
                val += dp[j]   
            }            
            maxVal = myMax(val, maxVal)
        }
        dp[i] = maxVal
        maxScore = myMax(maxScore, dp[i])
    }
    return maxScore
}

func myMax(i, j int) int {
	if i >= j {
		return i
	}
	return j
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	scores := StringToIntArray(flds[0])
	ages := StringToIntArray(flds[1])

	fmt.Printf("scores = %s\n", IntArrayToString(scores))
	fmt.Printf("ages = %s\n", IntArrayToString(ages))

	timeStart := time.Now()

	result := bestTeamScore(scores, ages)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

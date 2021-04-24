package solution

import (
	"fmt"
    "math"
    "strconv"
	"strings"
	"time"
)

func networkDelayTime(times [][]int, n int, k int) int {
    // 56ms
    graph := make([][]int, n)
    for i := 0; i < len(graph); i++ {
        graph[i] = make([]int, n)
    }

    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            graph[i][j] = math.MaxInt64;
        }
    }

    for i := 0; i < len(times); i++ {
        graph[times[i][0] - 1][times[i][1] - 1] = times[i][2];
    }

    dist := make([]int, n)
    visited := make([]bool, n);
    visited[k - 1] = true
    for i := 0; i < n; i++ {
        dist[i] = graph[k - 1][i]
    }
    dist[k - 1] = 0
    
    for i := 0; i < n - 1; i++ {
        min := math.MaxInt64
        pos := -1
        for j := 0; j < n; j++ {
            if !visited[j] && dist[j] < min {
                min = dist[j]
                pos = j
            }
        }
        if pos == -1 {
            break
        }
        visited[pos] = true
        for k2 := 0; k2 < n; k2++ {
            if graph[pos][k2] != math.MaxInt64 {
                if dist[k2] > dist[pos] + graph[pos][k2] {
                    dist[k2] = dist[pos] + graph[pos][k2]
                }
            }
        }
    }
    res := 0
    for i := 0; i < n; i++ {
        res = myMax(res, dist[i])
    }
    if res == math.MaxInt64 {
        return -1
    }
    return res
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
	temp = strings.Replace(temp, "[[[", "", -1)
	flds := strings.Split(temp, "]],[")
    flds0 := strings.Split(flds[0], "],[")
    times := make([][]int, len(flds0))
    for i := 0; i < len(times); i++ {
        times[i] = StringToIntArray(flds0[i])
    }
    flds1 := strings.Split(strings.Replace(flds[1], "]]", "", -1), "],[")
	n, _ := strconv.Atoi(flds1[0])
	k, _ := strconv.Atoi(flds1[1])

	fmt.Printf("times = %s, n = %d, k = %d\n", IntIntArrayToString(times), n, k)

	timeStart := time.Now()

	result := networkDelayTime(times, n, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

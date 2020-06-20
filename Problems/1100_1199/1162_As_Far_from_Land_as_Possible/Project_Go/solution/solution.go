package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func maxDistance(grid [][]int) int {
	// 844ms
	max_dist := -1
	N := len(grid)
	for i, row := range grid {
		for j, g := range row {
			if g == 0 {
				dist := -1
				min_dist := -1
				for d_i := 0; d_i < N; d_i++ {
					for d_j := 0; d_j <= N; d_j++ {
						if d_i > 0 || d_j > 0 {
							sum := 0
							if i-d_i >= 0 {
								if j-d_j >= 0 {
									sum += grid[i-d_i][j-d_j]
								}
								if j+d_j < N {
									sum += grid[i-d_i][j+d_j]
								}
							}
							if i+d_i < N {
								if j-d_j >= 0 {
									sum += grid[i+d_i][j-d_j]
								}
								if j+d_j < N {
									sum += grid[i+d_i][j+d_j]
								}
							}

							if sum > 0 {
								dist = d_i + d_j
								break
							}
						}
					}
					if dist > 0 {
						if min_dist < 0 || dist < min_dist {
							min_dist = dist
						}
					}
				}
				if min_dist > max_dist {
					max_dist = min_dist
				}
			}
		}
	}
	return max_dist
}

func maxDistance2(grid [][]int) int {
	// 1256ms
	queues := make([][2]int, 0)
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == 1 {
				queues = append(queues, [2]int{i, j})
			}
		}
	}
	if len(queues) == 0 || len(queues) == len(grid)*len(grid[0]) {
		return -1
	}
	var maxDistance int
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == 1 {
				continue
			}

			currentMin := math.MaxInt32
			for _, queue := range queues {
				current := int(myAbs(queue[0]-i) + myAbs(queue[1]-j))
				if current < currentMin {
					currentMin = current
				}
			}
			if currentMin > maxDistance {
				maxDistance = currentMin
			}
		}
	}

	return maxDistance
}

func myAbs(a int) int {
	if a > 0 {
		return a
	}

	return -a
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)
	grid_str := strings.Split(flds, "],[")

	grid := make([][]int, len(grid_str))
	for i := 0; i < len(grid_str); i++ {
		grid[i] = StringToIntArray(grid_str[i])
	}
	fmt.Printf("grid = %s\n", IntIntArrayToGridString(grid))

	timeStart := time.Now()

	result := maxDistance(grid)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

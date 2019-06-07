package main

import (
	"fmt"
	"strings"
	"time"
)

/*
   public List<String> commonChars(String[] A) {
       // 4ms
       int[][] charCount = new int[A.length][26];
       for (int i = 0; i < A.length; i++) {
           for (char c : A[i].toCharArray()) {
               charCount[i][c - 'a']++;
           }
       }

       List<String> result = new ArrayList<>();
       for (int i = 0; i < 26; i++) {
           while (charCount[0][i] != 0) {
               char c = (char) (i + 'a');
               boolean valid = true;
               charCount[0][i]--;
               for (int j = 1; j < A.length; j++) {
                   if (charCount[j][i] == 0) {
                       valid = false;
                       break;
                   } else {
                       charCount[j][i]--;
                   }
               }
               if (!valid) {
                   break;
               } else {
                   result.add("" + c);
               }
           }
       }
       return result;
   }
*/
func commonChars(A []string) []string {
	charCount := make([][]int, len(A))
	for i, _ := range charCount {
		charCount[i] = make([]int, 26)
	}

	for i := 0; i < len(A); i++ {
		for _, ch := range A[i] {
			charCount[i][ch-'a']++
		}
	}

	var result []string
	for i := 0; i < 26; i++ {
		for charCount[0][i] != 0 {
			c := i + 'a'
			valid := true
			charCount[0][i]--
			for j := 1; j < len(A); j++ {
				if charCount[j][i] == 0 {
					valid = false
					break
				} else {
					charCount[j][i]--
				}
			}
			if !valid {
				break
			} else {
				result = append(result, string(c))
			}
		}
	}
	return result
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	A := strings.Split(temp, ",")

	fmt.Printf("A = %s\n", A)

	timeStart := time.Now()

	result := commonChars(A)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}

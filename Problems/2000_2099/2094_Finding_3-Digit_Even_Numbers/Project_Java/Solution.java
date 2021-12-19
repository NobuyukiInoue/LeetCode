import java.util.*;

public class Solution {
    public int[] findEvenNumbers(int[] digits) {
        // 3ms
        int digCnt[] = new int[10];
        for (int digit : digits) {
            digCnt[digit]++;
        }
        ArrayList<Integer> res = new ArrayList<>();
        for(int i = 1; i < 10; i++){
            for (int j = 0; j < 10 && digCnt[i] > 0; j++) {
                for (int k = 0; k < 10 && digCnt[j] > ((i == j) ? 1 : 0); k += 2) {
                    int kJEq = (k == j) ? 1 : 0;
                    int kIEq = (k == i) ? 1 : 0;
                    if (digCnt[k] > (kJEq + kIEq)) {
                        int num = i*100 + j*10 + k;
                        res.add(num);
                    }
                }
            }
        }
        // 5ms
        // return res.stream().mapToInt(i->i).toArray();

        // 3ms
        int resArr[] = new int[res.size()];
        int index = 0;
        for (int elem : res) {
            resArr[index++] = elem;
        }
        return resArr;
    }

    public int[] findEvenNumbers2(int[] digits) {
        // 7ms
        HashMap<Integer, Integer> numof = new HashMap<>();
        for (int digit : digits) {
            numof.put(digit, numof.getOrDefault(digit, 0) + 1);
        }

        List<Integer> events = new ArrayList<>();
        List<Integer> hundreds = new ArrayList<>();
        for (int digit : numof.keySet()) {
            if ((digit & 1) == 0) {
                events.add(digit);
            }
            if (digit > 0) {
                hundreds.add(digit);
            }
        }
        List<Integer> ans = new ArrayList<>();
        for (int a : hundreds) {
            for (int b : numof.keySet()) {
                for (int c : events) {
                    int ab = (a == b)? 1 : 0;
                    int bc = (b == c)? 1 : 0;
                    int ca = (c == a)? 1 : 0;
                    if ((numof.get(a) > ab + ca) &&
                        (numof.get(b) > ab + bc) &&
                        (numof.get(c) > ca + bc))
                        ans.add(100*a + 10*b + c);
                }
            }
        }
        // 10ms
        // return ans.stream().mapToInt(i->i).toArray();

        // 7ms
        int resArr[] = new int[ans.size()];
        int index = 0;
        for (int elem : ans) {
            resArr[index++] = elem;
        }
        return resArr;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] digits = ml.stringToIntArray(flds);
        System.out.println("digits = " + ml.intArrayToString(digits));

        long start = System.currentTimeMillis();

        int[] result = findEvenNumbers(digits);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

import java.util.*;

public class Solution {
    public String pushDominoes(String dominoes) {
        // 9ms
        dominoes = "L" + dominoes + "R";
        StringBuilder res = new StringBuilder();
        int left = 0;
        for (int right = 1; right < dominoes.length(); right++) {
            if (dominoes.charAt(right) == '.') {
                continue;
            }
            int middle = right - left - 1;
            if (left > 0) {
                res.append(dominoes.charAt(left));
            }
            if (dominoes.charAt(left) == dominoes.charAt(right)) {
                for (int count = 0; count < middle; count++)
                    res.append(dominoes.charAt(left));
            } else if (dominoes.charAt(left) == 'L' && dominoes.charAt(right) == 'R') {
                for (int count = 0; count < middle; count++)
                    res.append('.');
            } else {
                for (int count = 0; count < middle / 2; count++)
                    res.append('R');
                for (int count = 0; count < middle % 2; count++)
                    res.append('.');
                for (int count = 0; count < middle / 2; count++)
                    res.append('L');
            }
            left = right;
        }
        return res.toString();
    }

    public void Main(String temp) {
        String dominoes = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("dominoes = " + dominoes);

        long start = System.currentTimeMillis();

        String result = pushDominoes(dominoes);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

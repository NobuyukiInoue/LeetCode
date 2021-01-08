import java.util.*;

public class Solution {
    public String originalDigits(String s) {
        // 8ms
        int[] count = new int[10];
        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if (c == 'z') count[0]++;
            if (c == 'w') count[2]++;
            if (c == 'x') count[6]++;
            if (c == 's') count[7]++; //7-6
            if (c == 'g') count[8]++;
            if (c == 'u') count[4]++; 
            if (c == 'f') count[5]++; //5-4
            if (c == 'h') count[3]++; //3-8
            if (c == 'i') count[9]++; //9-8-5-6
            if (c == 'o') count[1]++; //1-0-2-4
        }
        count[7] -= count[6];
        count[5] -= count[4];
        count[3] -= count[8];
        count[9] = count[9] - count[8] - count[5] - count[6];
        count[1] = count[1] - count[0] - count[2] - count[4];
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i <= 9; i++){
            for (int j = 0; j < count[i]; j++){
                sb.append(i);
            }
        }
        return sb.toString();
    }

    public String originalDigits2(String s) {
        // 15ms
        class MyMap {
            String word;
            char ch;
            public MyMap(String w, char c) {
                word = w;
                ch = c;
            }
        }

        MyMap[] mymap = new MyMap[] {
            new MyMap("zero", 'z'),
            new MyMap("one", 'o'), 
            new MyMap("two", 'w'),
            new MyMap("three", 'h'),
            new MyMap("four", 'u'),
            new MyMap("five", 'f'),
            new MyMap("six", 'x'),
            new MyMap("seven", 's'),
            new MyMap("eight", 'g'),
            new MyMap("nine", 'i')
        };
        
        HashMap<Character, Integer> cnt = new HashMap<>();
        for (Character ch : s.toCharArray()) {
            cnt.put(ch, cnt.getOrDefault(ch, 0) + 1);
        }

        StringBuilder ret = new StringBuilder();
        int[] i_list = new int[] {0, 2, 4, 6, 8, 1, 3, 5, 7, 9};
        for (int i : i_list) {
            if (!cnt.containsKey(mymap[i].ch))
                continue;

            int n = cnt.get(mymap[i].ch);
            if (n == 0)
                continue;
            for (char ch : mymap[i].word.toCharArray()) {
                cnt.put(ch, cnt.get(ch) - n);
            }

            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < n; j++) {
                sb.append(Integer.toString(i));
            }
            ret.append(sb);
        }

        char[] temp = ret.toString().toCharArray();
        Arrays.sort(temp);
        return new String(temp);
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        String result = originalDigits(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

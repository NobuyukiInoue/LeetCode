import java.util.*;

public class Solution {
    public String maximumBinaryString(String binary) {
        // 31ms
        int ones = 0, zeros = 0, n = binary.length();
        StringBuilder res = new StringBuilder("1".repeat(n));
        for (int i = 0; i < n; ++i) {
            if (binary.charAt(i) == '0') {
                zeros++;
            } else if (zeros == 0) {
                ones++;
            }
        }
        if (ones < n) {
            res.setCharAt(ones + zeros - 1, '0');
        }
        return res.toString();
    }

    public String maximumBinaryString2(String binary) {
        // 45ms
        int count = 0, index = -1;
        for (int i = binary.length() - 1; i >= 0; i--) {
            count += (49 - binary.charAt(i));
            index = (binary.charAt(i) == '0') ? i : index;
        }
        char[] data = new char[binary.length()];
        Arrays.fill(data, '1');
        if (index != -1) {
            data[index + count - 1] = '0';
        }
        return new String(data);
    }

    public void Main(String temp) {
        String binary = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("binary = " + binary);

        long start = System.currentTimeMillis();

        String result = maximumBinaryString(binary);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}

import java.util.*;

public class Solution {
    public String oddString(String[] words) {
        // 3ms
		HashMap<String, List<String>> cnts = new HashMap<>();
		String res = "";
		for (String word: words) {
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < word.length() - 1; i ++) {
				sb.append(String.valueOf(word.charAt(i + 1) - word.charAt(i)));
				sb.append(',');
			}
			String diff = sb.toString();
			cnts.putIfAbsent(diff, new ArrayList<>());
			cnts.get(diff).add(word);
		}
		for (String diff: cnts.keySet()) {
			if (cnts.get(diff).size() == 1) {
				res = cnts.get(diff).get(0);
				break;
			}
		}
		return res;
    }

    public void Main(String temp) {
        String[] words = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[", "").replace("]", "").split(",");
        Mylib ml = new Mylib();
        System.out.println("words = " + ml.stringArrayToString(words));
        long start = System.currentTimeMillis();

        String result = oddString(words);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

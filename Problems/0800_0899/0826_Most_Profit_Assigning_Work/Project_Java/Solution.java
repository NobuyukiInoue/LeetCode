import java.util.*;

public class Solution {
    public int maxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {
        // 12ms
        int[][]jobs = new int[difficulty.length][];
        for (int i = 0; i < jobs.length; i++) {
            jobs[i] = new int[] { difficulty[i], profit[i] };
        }
        Arrays.sort(jobs, (a, b) -> Integer.compare(a[0], b[0]));
        int res = 0, i = 0, best = 0;
        Arrays.sort(worker);
        for (int ability : worker) {
            while (i < jobs.length && ability >= jobs[i][0]) {
                best = Math.max(jobs[i][1], best);
                i++;
            }
            res += best;
        }
        return res;
    }

/*
    public int maxProfitAssignment2(int[] difficulty, int[] profit, int[] worker) {
        // 17ms
        List<Pair<Integer, Integer>> jobs = new ArrayList<>();
        int N = profit.length, res = 0, i = 0, best = 0;
        for (int j = 0; j < N; ++j)
            jobs.add(new Pair<Integer, Integer>(difficulty[j], profit[j]));
        Collections.sort(jobs, Comparator.comparing(Pair::getKey));
        Arrays.sort(worker);
        for (int ability : worker) {
            while (i < N && ability >= jobs.get(i).getKey())
                best = Math.max(jobs.get(i++).getValue(), best);
            res += best;
        }
        return res;
    }
*/

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] difficulty = ml.stringToIntArray(flds[0]);
        int[] profit     = ml.stringToIntArray(flds[1]);
        int[] worker     = ml.stringToIntArray(flds[2]);

        System.out.println("difficulty = " + ml.intArrayToString(difficulty));
        System.out.println("profit = " + ml.intArrayToString(profit));
        System.out.println("worker = " + ml.intArrayToString(worker));

        long start = System.currentTimeMillis();

        int result = maxProfitAssignment(difficulty, profit, worker);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

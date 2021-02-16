import java.util.*;

public class Solution {
    public boolean isNStraightHand(int[] hand, int W) {
        // 15ms
        Counter counter = new Counter();
        for (int num:hand)
            counter.add(num,1);
        for (int num:hand) {
            if (counter.get(num-1) > 0 || counter.get(num) == 0) {
                continue;
            } else {
                int currNum = num;
                while (counter.get(currNum) > 0) {
                    int count = 0;
                    int newStartingNum = -1;
                    while (count < W) {
                        if (counter.get(currNum) == 0) {
                            return false;
                        }
                        counter.add(currNum,-1);
                        if (newStartingNum == -1 && counter.get(currNum) > 0) {
                            newStartingNum = currNum;
                        }
                        currNum += 1;
                        count++;
                    }
                    currNum = (newStartingNum == -1 ? currNum : newStartingNum);
                }
            }
        }
        return true;
    }
    
    class Counter extends HashMap<Integer,Integer> {
        public int get(int key) {
            return this.containsKey(key) ? super.get(key) : 0;
        }
        
        public void add(int key, int num) {
            this.put(key, this.get(key) + num);
        }
    }

   public boolean isNStraightHand2(int[] hand, int W) {
        // 59ms
        Map<Integer, Integer> dic = new TreeMap<>();

        for (int i : hand) {
            dic.put(i, dic.getOrDefault(i, 0) + 1);
        }

        for (int it : dic.keySet()) {
            if (dic.get(it) > 0) {
                for (int i = W - 1; i >= 0; --i) {
                    if (dic.getOrDefault(it + i, 0) < dic.get(it)) return false;
                    dic.put(it + i, dic.get(it + i) - dic.get(it));
                }
            }
        }

        return true;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        Mylib ml = new Mylib();
        int[] hand = ml.stringToIntArray(flds[0]);
        int W = Integer.parseInt(flds[1]);
        System.out.println("hand = " + ml.intArrayToString(hand) + ", W = " + Integer.toString(W));

        long start = System.currentTimeMillis();

        boolean result = isNStraightHand(hand, W);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

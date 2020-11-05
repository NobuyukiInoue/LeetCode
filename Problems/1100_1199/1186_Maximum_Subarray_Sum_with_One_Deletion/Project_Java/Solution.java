public class Solution {
    public int maximumSum(int[] arr) {
        // 6ms
        int[] withDelete    = new int[arr.length];
        int[] withOutDelete = new int[arr.length];
        int result = Integer.MIN_VALUE;
        int start = 0;
        while (start < arr.length && arr[start] < 0) {
            result = Math.max(result, arr[start++]);
        }
        
        for (int i = start; i < arr.length; i++) {
            if (arr[i] >= 0) {
                if (i == 0) {
                    withOutDelete[i] = arr[i];
                    withDelete[i]    = arr[i];
                } else {
                    withOutDelete[i] = Math.max(withOutDelete[i - 1] + arr[i], arr[i]);
                    withDelete[i]    = Math.max(withDelete[i - 1] + arr[i], arr[i]);
                }
            } else {
                if (i > 0) {
                    withOutDelete[i] = Math.max(withOutDelete[i - 1] + arr[i], arr[i]);
                    withDelete[i]    = Math.max(withOutDelete[i - 1], withDelete[i - 1] + arr[i]);
                }
            }
            result = Math.max(result, withOutDelete[i]);
            result = Math.max(result, withDelete[i]);
        }
        
        return result;
    }

    public int maximumSum2(int[] arr) {
        // 7ms
        int notused = 0, used = 0, res = arr[0];
        for (int num : arr) {
            if (num >= 0) {
                notused += num;
                used += num;
            } else {
                notused = Math.max(notused + num, used);
                used += num;
            }

            int val1, val2;

            if (notused != 0)
                val1 = notused;
            else
                val1 = Integer.MIN_VALUE;

            if (used != 0)
                val2 = used;
            else
                val2 = Integer.MIN_VALUE;

            res = myMax3(res, val1, val2);

            if (notused < 0)
                notused = 0;
            if (used < 0)
                used = 0;
        }
        return Math.max(res, arrMax(arr));
    }

    private int myMax3(int a, int b, int c) {
        if (a >= b && a >= c)
            return a;
        else if (b >= a && b >= c)
            return b;
        return c;
    }

    private int arrMax(int[] arr) {
        int max = Integer.MIN_VALUE;
        for (int num : arr)
            if (num > max)
                max = num;
        return max;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] arr = ml.stringToIntArray(flds);
        System.out.println("arr = " + ml.intArrayToString(arr));

        long start = System.currentTimeMillis();

        int result = maximumSum(arr);

        long end = System.currentTimeMillis();

        System.out.println(String.format("result = %d", result));
        System.out.println((end - start)  + "ms\n");
    }
}

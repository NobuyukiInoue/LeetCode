public class Solution {

    public int[] replaceElements(int[] arr) {
        // 1ms
        for (int i = arr.length - 1, mx = -1; i >= 0; --i)
            mx = Math.max(arr[i], arr[i] = mx);
        return arr;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib mc = new Mylib();
        int[] arr = mc.stringTointArray(flds);

        System.out.println("arr = " + mc.intArrayToString(arr));

        long start = System.currentTimeMillis();

        int[] result = replaceElements(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + mc.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

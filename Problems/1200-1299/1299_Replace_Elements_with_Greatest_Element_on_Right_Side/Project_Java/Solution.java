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
        int[] arr = mc.str_to_int_array(flds);

        System.out.println("arr = " + mc.output_int_array(arr));

        long start = System.currentTimeMillis();

        int[] result = replaceElements(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + mc.output_int_array(result));
        System.out.println((end - start)  + "ms\n");
    }
}

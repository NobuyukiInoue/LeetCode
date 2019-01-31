import java.io.File;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        if (args.length != 1) {
            final String className = new Object(){}.getClass().getEnclosingClass().getName();
            System.out.println("Usage:" + className + " <testdata.txt>");
            System.exit(1);
        }

        try {
            File file = new File(args[0]);

            BufferedReader br = new BufferedReader(new FileReader(file));
            String str = br.readLine();
            while(str != null){
                System.out.println(str);
                loop_main(str);
                str = br.readLine();
            }

            br.close();

        } catch(FileNotFoundException e) {
            System.out.println(e);
        } catch(IOException e) {
            System.out.println(e);
        }
    }

    public static void loop_main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib mc = new Mylib();
        int[] nums = mc.str_to_int_array(flds[0]);
        int target = Integer.parseInt(flds[1]);

        System.out.println("nums = " + mc.output_int_array(nums));
        System.out.println("target = " + String.valueOf(target));

        long start = System.currentTimeMillis();
        
        Solution sl = new Solution();
        int[] result = sl.twoSum(nums, target);

        long end = System.currentTimeMillis();

        System.out.println("result = " + mc.output_int_array(result));
        System.out.println((end - start)  + "ms\n");
    }
}

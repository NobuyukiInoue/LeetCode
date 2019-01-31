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
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        String s = flds[0];
        String t = flds[1];

        System.out.println("s = " + s + ", t = " + t);

        long start = System.currentTimeMillis();

        Solution sl = new Solution();
        char result = sl.findTheDifference(s, t);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms");
    }
}

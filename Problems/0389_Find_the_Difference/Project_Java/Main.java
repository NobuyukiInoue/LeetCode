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

        if ((new File(args[0])).exists() == false) {
            System.out.println(args[0] + " not found.");
            System.exit(1);
        }

        try {
            File file = new File(args[0]);

            BufferedReader br = new BufferedReader(new FileReader(file));
            String str = br.readLine();

            Solution sl = new Solution();
            while(str != null){
                System.out.println(str);
                sl.Main(str);
                str = br.readLine();
            }

            br.close();
            sl = null;

        } catch(FileNotFoundException e) {
            System.out.println(e);
        } catch(IOException e) {
            System.out.println(e);
        }
    }
}

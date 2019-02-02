import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);

        long start = System.currentTimeMillis();


        String str = null;
        System.out.println("Hit Enter Key.");

        try {
            str = br.readLine();
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        long end = System.currentTimeMillis();

        System.out.println(Long.toString(start)  + "ms\n");
        System.out.println(Long.toString(end)  + "ms\n");
        System.out.println(Long.toString(end - start)  + "ms\n");
    }
}

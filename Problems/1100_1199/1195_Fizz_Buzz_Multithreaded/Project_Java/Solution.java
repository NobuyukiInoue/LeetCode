import java.util.function.IntConsumer;

public class Solution {
    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int n = Integer.parseInt(fld);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        FizzBuzz fz = new FizzBuzz(n);

        class ThreadFizz extends Thread {
            class FuncFizz implements Runnable {
                @Override
                public void run() {
                    System.out.print(" fizz");
                }
            }
    
            FuncFizz funcFizz = new FuncFizz();

            @Override
            public void run() {
                try {
                    fz.fizz(funcFizz);
                } catch (Exception e) {
                    if (e.getMessage() != null)
                        System.out.println(e.getMessage());
                    System.exit(1);
                }
            }
        }

        class ThreadBuzz extends Thread {
            class FuncBuzz implements Runnable {
                @Override
                public void run() {
                    System.out.print(" buzz");
                }
            }
    
            FuncBuzz funcBuzz = new FuncBuzz();

            @Override
            public void run() {
                try {
                    fz.buzz(funcBuzz);
                } catch (Exception e) {
                    if (e.getMessage() != null)
                        System.out.println(e.getMessage());
                    System.exit(1);
                }
            }
        }

        class ThreadFizzBuzz extends Thread {
            class FuncFizzBuzz implements Runnable {
                @Override
                public void run() {
                    System.out.print(" fizzbuzz");
                }
            }
    
            FuncFizzBuzz funcFizzBuzz = new FuncFizzBuzz();

            @Override
            public void run() {
                try {
                    fz.fizzbuzz(funcFizzBuzz);
                } catch (Exception e) {
                    if (e.getMessage() != null)
                        System.out.println(e.getMessage());
                    System.exit(1);
                }
            }
        }


        class ThreadNumber extends Thread {
            class FuncNumber implements IntConsumer {
                @Override
                public void accept(int i) {
                    System.out.print(" " + Integer.toString(i));
                }
            }

            FuncNumber funcNumber = new FuncNumber();

            @Override
            public void run() {
                try {
                    fz.number(funcNumber);
                } catch (Exception e) {
                    if (e.getMessage() != null)
                        System.out.println(e.getMessage());
                    System.exit(1);
                }
            }
        }
        
        ThreadFizz threadFizz = new ThreadFizz();
        ThreadBuzz threadBuzz = new ThreadBuzz();
        ThreadFizzBuzz threadFizzBuzz = new ThreadFizzBuzz();
        ThreadNumber threadNumber = new ThreadNumber();

        threadFizz.start();
        threadBuzz.start();
        threadFizzBuzz.start();
        threadNumber.start();

        // Wait until the thread ends.
		try {
			threadFizz.join();
			threadBuzz.join();
            threadFizzBuzz.join();
            threadNumber.join();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}

        long end = System.currentTimeMillis();

        System.out.println("\n");
        System.out.println((end - start)  + "ms\n");
    }
}

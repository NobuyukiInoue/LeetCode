import java.util.function.IntConsumer;

public class Solution {
    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int n = Integer.parseInt(fld);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        ZeroEvenOdd zeroEvenOdd = new ZeroEvenOdd(n);

        class ThreadZero extends Thread {
            class PrintNumber implements IntConsumer {
                @Override
                public void accept(int i) {
                    System.out.print(Integer.toString(i));
                }
            }

            PrintNumber printNumber = new PrintNumber();

            @Override
            public void run() {
                try {
                    zeroEvenOdd.zero(printNumber);
                } catch (Exception e) {
                    if (e.getMessage() != null)
                        System.out.println(e.getMessage());
                    System.exit(1);
                }
            }
        }

        class ThreadEven extends Thread {
            class PrintNumber implements IntConsumer {
                @Override
                public void accept(int i) {
                    System.out.print(Integer.toString(i));
                }
            }

            PrintNumber printNumber = new PrintNumber();

            @Override
            public void run() {
                try {
                    zeroEvenOdd.even(printNumber);
                } catch (Exception e) {
                    if (e.getMessage() != null)
                        System.out.println(e.getMessage());
                    System.exit(1);
                }
            }
        }

        class ThreadOdd extends Thread {
            class PrintNumber implements IntConsumer {
                @Override
                public void accept(int i) {
                    System.out.print(Integer.toString(i));
                }
            }

            PrintNumber printNumber = new PrintNumber();

            @Override
            public void run() {
                try {
                    zeroEvenOdd.odd(printNumber);
                } catch (Exception e) {
                    if (e.getMessage() != null)
                        System.out.println(e.getMessage());
                    System.exit(1);
                }
            }
        }

        ThreadZero threadZero = new ThreadZero();
        ThreadEven threadEven = new ThreadEven();
        ThreadOdd threadOdd = new ThreadOdd();
        threadZero.start();
        threadEven.start();
        threadOdd.start();

        // Wait until the thread ends.
        try {
			threadZero.join();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
        
        // Wait until the thread ends.
		try {
			threadEven.join();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}

        // Wait until the thread ends.
		try {
			threadOdd.join();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}


        long end = System.currentTimeMillis();

        System.out.println("\n");
        System.out.println((end - start)  + "ms\n");
    }
}

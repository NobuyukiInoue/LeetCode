import java.util.function.IntConsumer;

public class Solution {
    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int n = Integer.parseInt(fld);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        FooBar fb = new FooBar(n);

        class ThreadFoo extends Thread {
            class FuncFoo implements Runnable {
                @Override
                public void run() {
                    System.out.print("foo");
                }
            }
    
            FuncFoo funcFoo = new FuncFoo();

            @Override
            public void run() {
                try {
                    fb.foo(funcFoo);
                } catch (Exception e) {
                    if (e.getMessage() != null)
                        System.out.println(e.getMessage());
                    System.exit(1);
                }
            }
        }

        class ThreadBar extends Thread {
            class FuncBar implements Runnable {
                @Override
                public void run() {
                    System.out.print("bar");
                }
            }
    
            FuncBar funcBar = new FuncBar();

            @Override
            public void run() {
                try {
                    fb.bar(funcBar);
                } catch (Exception e) {
                    if (e.getMessage() != null)
                        System.out.println(e.getMessage());
                    System.exit(1);
                }
            }
        }

        ThreadFoo threadFoo = new ThreadFoo();
        ThreadBar threadBar = new ThreadBar();

        threadFoo.start();
        threadBar.start();

        // Wait until the thread ends.
		try {
			threadFoo.join();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
        
        // Wait until the thread ends.
		try {
			threadBar.join();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}

        long end = System.currentTimeMillis();

        System.out.println("\n");
        System.out.println((end - start)  + "ms\n");
    }
}

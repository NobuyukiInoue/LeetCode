public class Solution {
    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(fld);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        Foo foo = new Foo();

        class ThreadFirst extends Thread {
            class FuncFirst implements Runnable {
                @Override
                public void run() {
                    System.out.print("first");
                }
            }
    
            FuncFirst funcFirst = new FuncFirst();

            @Override
            public void run() {
                try {
                    foo.first(funcFirst);
                } catch (Exception e) {
                    if (e.getMessage() != null)
                        System.out.println(e.getMessage());
                    System.exit(1);
                }
            }
        }

        class ThreadSecond extends Thread {
            class FuncSecond implements Runnable {
                @Override
                public void run() {
                    System.out.print("second");
                }
            }
    
            FuncSecond funcSecond = new FuncSecond();

            @Override
            public void run() {
                try {
                    foo.second(funcSecond);
                } catch (Exception e) {
                    if (e.getMessage() != null)
                        System.out.println(e.getMessage());
                    System.exit(1);
                }
            }
        }

        class ThreadThird extends Thread {
            class FuncThird implements Runnable {
                @Override
                public void run() {
                    System.out.print("third");
                }
            }
    
            FuncThird funcThird = new FuncThird();

            @Override
            public void run() {
                try {
                    foo.third(funcThird);
                } catch (Exception e) {
                    if (e.getMessage() != null)
                        System.out.println(e.getMessage());
                    System.exit(1);
                }
            }
        }

        ThreadFirst ThreadFirst = new ThreadFirst();
        ThreadSecond ThreadSecond = new ThreadSecond();
        ThreadThird ThreadThird = new ThreadThird();

        for (int num : nums) {
            switch (num) {
            case 1:
                ThreadFirst.start();
                break;
            case 2:
                ThreadSecond.start();
                break;
            case 3:
                ThreadThird.start();
                break;
            }
        }

        // Wait until the thread ends.
		try {
			ThreadFirst.join();
			ThreadSecond.join();
			ThreadThird.join();

        } catch (InterruptedException e) {
			e.printStackTrace();
		}

        long end = System.currentTimeMillis();

        System.out.println("\n");
        System.out.println((end - start)  + "ms\n");
    }
}

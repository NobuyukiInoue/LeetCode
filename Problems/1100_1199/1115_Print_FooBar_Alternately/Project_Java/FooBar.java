import java.util.function.*;
import java.util.concurrent.*;

class FooBar {
    // 17ms
    private int n;
    private Semaphore sem_foo, sem_bar;

    public FooBar(int n) {
        this.n = n;
        sem_foo = new Semaphore(1);
        sem_bar = new Semaphore(0);
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            sem_foo.acquire();

            // printFoo.run() outputs "foo". Do not change or remove this line.
        	printFoo.run();

            sem_bar.release();
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            sem_bar.acquire();

            // printBar.run() outputs "bar". Do not change or remove this line.
        	printBar.run();

            sem_foo.release();
        }
    }
}

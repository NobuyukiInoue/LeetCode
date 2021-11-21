import java.util.concurrent.*;

class Foo {
    // 9ms
    private Semaphore sem_second, sem_third;

    public Foo() {
        sem_second = new Semaphore(0);
        sem_third = new Semaphore(0);
    }

    public void first(Runnable printFirst) throws InterruptedException {
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        sem_second.release();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        // printSecond.run() outputs "second". Do not change or remove this line.
        sem_second.acquire();
        printSecond.run();
        sem_third.release();
    }

    public void third(Runnable printThird) throws InterruptedException {
        // printThird.run() outputs "third". Do not change or remove this line.
        sem_third.acquire();
        printThird.run();
    }
}

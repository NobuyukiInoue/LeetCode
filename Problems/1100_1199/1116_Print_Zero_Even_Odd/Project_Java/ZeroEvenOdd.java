import java.util.concurrent.*;
import java.util.function.IntConsumer;

class ZeroEvenOdd {
    // 7ms
    private int n;
    private Semaphore sem_zero, sem_even, sem_odd;
    
    public ZeroEvenOdd(int n) {
        this.n = n;
        sem_zero = new Semaphore(1);
        sem_even = new Semaphore(0);
        sem_odd = new Semaphore(0);
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void zero(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i < n + 1; i++) {
            sem_zero.acquire();
            printNumber.accept(0);
            if (i % 2 == 1) {
                sem_odd.release();
            } else {
                sem_even.release();
            }
        }
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        for (int i = 2; i < n + 1; i += 2) {
            sem_even.acquire();
            printNumber.accept(i);
            sem_zero.release();
        }
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i < n + 1; i += 2) {
            sem_odd.acquire();
            printNumber.accept(i);
            sem_zero.release();
        }
    }
}

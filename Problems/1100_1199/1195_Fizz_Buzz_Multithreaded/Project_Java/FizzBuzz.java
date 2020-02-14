import java.util.function.*;
import java.util.concurrent.*;

class FizzBuzz {
    // 6ms
    private int n;
    private Semaphore sem_fizz, sem_buzz, sem_fizzbuzz, sem_number;
    boolean finished = false;

    public FizzBuzz(int n) {
        this.n = n;
        sem_number = new Semaphore(1);
        sem_fizz = new Semaphore(0);
        sem_buzz = new Semaphore(0);
        sem_fizzbuzz = new Semaphore(0);
    }

    // printFizz.run() outputs "fizz".
    public void fizz(Runnable printFizz) throws InterruptedException {
        for (int i = 3; i <= n; i += 3) {
            sem_fizz.acquire();
            printFizz.run();
            if ((i + 3) % 5 == 0) // skip multiples of 15.
                i += 3;
            sem_number.release();
        }      
    }

    // printBuzz.run() outputs "buzz".
    public void buzz(Runnable printBuzz) throws InterruptedException {
        for (int i = 5; i <= n; i += 5) {
            sem_buzz.acquire();
            printBuzz.run();
            if ((i + 5) % 3 == 0) // skip multiples of 15.
                i += 5;
            sem_number.release();
        }    
    }

    // printFizzBuzz.run() outputs "fizzbuzz".
    public void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
        for (int i = 15; i <= n; i += 15) {
            sem_fizzbuzz.acquire();
            printFizzBuzz.run();
            sem_number.release();
        }
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void number(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= n; i++) {
            sem_number.acquire();
            if (i % 15 == 0) {
                sem_fizzbuzz.release();
            } else if (i % 5 == 0) {
                sem_buzz.release();
            } else if (i % 3 == 0) {
                sem_fizz.release();
            } else {
                printNumber.accept(i);
                sem_number.release();
            }
        }

        finished = true;
    }

    public boolean isFinished() {
        return finished;
    }
}
